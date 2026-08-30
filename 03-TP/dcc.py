"""DCC-GARCH à deux étapes (Engle 2002) — corrigés Python.

Économétrie financière — M2 (Paris 8 / Créteil)

`Python` n'a pas d'équivalent direct à `rmgarch` : ce module reconstruit
l'estimateur en deux étapes vu en cours (chapitre 4) et fait ce que fait
`rmgarch::dccfit` — mais fait par vous, ce qui a l'avantage pédagogique de
rendre visible la décomposition Q1L_T(theta_V) + Q2L_T(theta_R) plutôt que
de la cacher dans un package.

Étape 1 : un GARCH(1,1) univarié par actif (`arch`), d'où les résidus
standardisés epsilon_t = r_t / sigma_t.
Étape 2 : la dynamique de corrélation, par QMLE sur la vraisemblance de
corrélation conditionnelle à epsilon_t donné (Engle 2002, éq. 17) :

    Q_t = (1 - a - b) * Qbar + a * epsilon_{t-1} epsilon_{t-1}' + b * Q_{t-1}
    R_t = diag(Q_t)^{-1/2} Q_t diag(Q_t)^{-1/2}

Un CCC (corrélation constante, Bollerslev 1990) est le cas particulier
a = b = 0 : R_t = Qbar pour tout t, sans optimisation.
"""

import numpy as np
import pandas as pd
from arch import arch_model
from scipy.optimize import minimize


class DCCGARCH:
    """DCC-GARCH(1,1) à deux étapes sur un DataFrame de rendements (colonnes = actifs)."""

    def __init__(self, returns: pd.DataFrame, dist: str = "normal"):
        self.returns = returns
        self.assets = list(returns.columns)
        self.dist = dist
        self.uni_fits_ = {}

    def _fit_univariate(self):
        std_resid, sigma = {}, {}
        for name in self.assets:
            am = arch_model(self.returns[name], mean="Constant",
                             vol="GARCH", p=1, q=1, dist=self.dist)
            res = am.fit(disp="off")
            self.uni_fits_[name] = res
            std_resid[name] = res.std_resid
            sigma[name] = res.conditional_volatility
        self.std_resid_ = pd.DataFrame(std_resid, index=self.returns.index)
        self.sigma_ = pd.DataFrame(sigma, index=self.returns.index)

    @staticmethod
    def _recursion(E, a, b, Qbar):
        T, N = E.shape
        Q = np.empty((T, N, N))
        Q[0] = Qbar
        for t in range(1, T):
            Q[t] = (1 - a - b) * Qbar + a * np.outer(E[t - 1], E[t - 1]) + b * Q[t - 1]
        return Q

    @staticmethod
    def _to_corr(Q):
        d = np.sqrt(np.diagonal(Q, axis1=-2, axis2=-1))
        d_inv = 1.0 / d
        return Q * d_inv[:, :, None] * d_inv[:, None, :]

    def _neg_loglik(self, params, E, Qbar):
        a, b = params
        if a < 0 or b < 0 or a + b >= 1:
            return 1e10
        R = self._to_corr(self._recursion(E, a, b, Qbar))
        ll = 0.0
        for t in range(E.shape[0]):
            sign, logdet = np.linalg.slogdet(R[t])
            if sign <= 0:
                return 1e10
            quad = E[t] @ np.linalg.solve(R[t], E[t])
            ll += -0.5 * (logdet + quad - E[t] @ E[t])
        return -ll

    def fit(self, dcc_order: tuple[int, int] = (1, 1)):
        """dcc_order=(1,1) pour un DCC ; (0,0) pour le cas emboîté CCC."""
        self._fit_univariate()
        E = self.std_resid_.to_numpy()
        Qbar = np.cov(E, rowvar=False)

        if dcc_order == (0, 0):
            self.theta_ = (0.0, 0.0)
        else:
            opt = minimize(self._neg_loglik, x0=[0.03, 0.90], args=(E, Qbar),
                            method="Nelder-Mead",
                            options={"xatol": 1e-8, "fatol": 1e-8, "maxiter": 3000})
            self.theta_ = tuple(opt.x)
            self.opt_result_ = opt

        self.Qbar_ = Qbar
        self.Q_ = self._recursion(E, *self.theta_, Qbar)
        self.R_ = self._to_corr(self.Q_)
        self.loglik_ = -self._neg_loglik(np.array(self.theta_), E, Qbar)
        return self

    def rcor(self) -> np.ndarray:
        """Corrélations conditionnelles estimées, tableau (T, N, N) — comme `rcor(fit)` en R."""
        return self.R_

    def rcov(self) -> np.ndarray:
        """Covariances conditionnelles H_t = D_t R_t D_t, tableau (T, N, N) — comme `rcov(fit)`."""
        N = len(self.assets)
        D = self.sigma_.to_numpy()[:, :, None] * np.eye(N)[None, :, :]
        return np.einsum("tij,tjk,tkl->til", D, self.R_, D)

    def rcor_pair(self, asset1: str, asset2: str) -> pd.Series:
        """Corrélation conditionnelle entre deux actifs, en série indexée par date."""
        i, j = self.assets.index(asset1), self.assets.index(asset2)
        return pd.Series(self.R_[:, i, j], index=self.returns.index, name=f"{asset1}-{asset2}")
