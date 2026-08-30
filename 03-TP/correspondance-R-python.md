# Correspondance `R` ↔ `Python`

**Économétrie financière · M2 (Paris 8 / Créteil)**

Les travaux sur machine se font au choix en `R` ou en `Python`. Ce document liste,
pour chaque opération du cours, la fonction à utiliser dans chaque écosystème.

Il n'est **pas** un cours de programmation : il suppose que vous savez déjà
manipuler un tableau de données dans le langage que vous avez choisi.

---

## Données et rendements

| Opération | `R` | `Python` |
|---|---|---|
| Télécharger des prix (Yahoo Finance) | `quantmod::getSymbols("^FCHI")` | `yfinance.download("^FCHI", auto_adjust=True)` |
| Prix de clôture ajustés | `quantmod::Ad(x)` (ou `Cl(x)` sur un objet déjà ajusté) | colonne `"Close"` (avec `auto_adjust=True`) |
| Rendement simple | `quantmod::dailyReturn(x, type = "arithmetic")` | `x.pct_change()` |
| Log-rendement | `quantmod::dailyReturn(x, type = "log")`, ou `diff(log(x))` | `np.log(x).diff()` |
| Graphique | `plot(x, type = "l")` | `fig, ax = plt.subplots(); ax.plot(x)` |
| Ligne horizontale | `abline(h = 0)` | `ax.axhline(0)` |

> **`yfinance` a changé plusieurs fois de convention.** Avec
> `auto_adjust=True` (comportement par défaut des versions récentes), la
> colonne `"Close"` est déjà le prix **ajusté** — il n'y a pas de colonne
> séparée `"Adj Close"`. Vérifiez toujours la version installée
> (`yfinance.__version__`) avant de comparer vos résultats à ceux d'un
> camarade.

---

## Statistiques descriptives et normalité

| Opération | `R` | `Python` |
|---|---|---|
| Asymétrie (skewness) | `moments::skewness(x)` | `scipy.stats.skew(x)` |
| Kurtosis (non centrée, normale = 3) | `moments::kurtosis(x)` | `scipy.stats.kurtosis(x, fisher=False)` |
| Test de Jarque-Bera | `tseries::jarque.bera.test(x)` | `statsmodels.stats.stattools.jarque_bera(x)` |
| QQ-plot | `qqnorm(x); qqline(x)` | `statsmodels.api.qqplot(x, line="s")` ou `scipy.stats.probplot(x, plot=ax)` |
| Histogramme + densité normale | `hist(x, freq = FALSE); curve(dnorm(...), add = TRUE)` | `ax.hist(x, density=True); ax.plot(grille, norm.pdf(grille, ...))` |

> **Attention à `fisher=`.** Par défaut, `scipy.stats.kurtosis()` renvoie la
> kurtosis **en excès** (normale = 0), pas la convention de `moments::kurtosis`
> (normale = 3). Oublier `fisher=False` décale silencieusement tous vos
> commentaires de 3.

---

## Tests de diagnostic sur les résidus

| Test | `H_0` | `R` | `Python` |
|---|---|---|---|
| Ljung-Box | absence d'autocorrélation | `Box.test(r, lag, type = "Ljung-Box")` | `statsmodels.stats.diagnostic.acorr_ljungbox(r, lags=[k])` |
| Jarque-Bera | normalité | `tseries::jarque.bera.test(r)` | `statsmodels.stats.stattools.jarque_bera(r)` |
| Engle ARCH | absence d'effet ARCH | `FinTS::ArchTest(r, lags)` | `statsmodels.stats.diagnostic.het_arch(r, nlags=k)` |
| White (hétéroscédasticité) | homoscédasticité | régression auxiliaire à la main, ou `lmtest::bptest` | `statsmodels.stats.diagnostic.het_white(r, X)`, ou à la main comme au TD2 |
| KPSS | stationnarité | `tseries::kpss.test(x)` | `statsmodels.tsa.stattools.kpss(x)`, ou `arch.unitroot.KPSS(x)` |
| ADF | racine unitaire | `tseries::adf.test(x)` | `statsmodels.tsa.stattools.adfuller(x)`, ou `arch.unitroot.ADF(x)` |

Rappel du chapitre 2 : ADF et KPSS n'ont pas la même hypothèse nulle. Un petit
$p$ ne veut donc pas dire la même chose selon le test.

---

## ARMA (chapitre 2)

| Opération | `R` | `Python` |
|---|---|---|
| Estimer un ARMA | `arima(x, order = c(p, 0, q))` | `statsmodels.tsa.arima.model.ARIMA(x, order=(p, 0, q)).fit()` |
| Sélection automatique | `forecast::auto.arima(x)` | pas d'équivalent fiable — voir note ci-dessous |
| Significativité des coefficients | `lmtest::coeftest(fit)` | `res.summary()` (colonnes `coef`, `std err`, `P>|z|`) |
| AIC / BIC | `AIC(fit)`, `BIC(fit)` | `res.aic`, `res.bic` |
| Résidus | `residuals(fit)` | `res.resid` |

> **`auto.arima` n'a pas de bon équivalent `Python`.** Le paquet le plus
> proche, `pmdarima` (`auto_arima`), dépend d'une extension C compilée
> contre une ABI `numpy` précise ; avec `numpy` ≥ 2.0 (l'installation par
> défaut de `pip install numpy` aujourd'hui), l'import échoue purement et
> simplement (`ValueError: numpy.dtype size changed...`), et rien ne
> garantit que ce sera résolu au moment où vous lirez ceci. Les corrigés
> reconstruisent le principe à la main : une boucle sur $(p,q) \in
> \{0,\dots,5\}^2$ qui retient le modèle au plus petit AIC — exactement ce
> que fait `auto.arima` en interne (recherche stepwise ou exhaustive par
> AIC), en plus transparent.

---

## Modèles ARCH / GARCH univariés (chapitre 3)

`rugarch` (`R`) et `arch` (`Python`, paquet `arch_model`) couvrent le même
terrain, avec une différence structurante : **`rugarch` sépare la
spécification (`ugarchspec`) de l'estimation (`ugarchfit`)**, alors que
`arch_model()` fait les deux en un objet à `.fit()`.

| Modèle | `R` (`rugarch::ugarchspec`) | `Python` (`arch.arch_model`) |
|---|---|---|
| ARCH(1) | `variance.model = list(model = "sGARCH", garchOrder = c(1,0))` | `vol="ARCH", p=1` (ou `vol="GARCH", p=1, q=0`) |
| GARCH(1,1) | `garchOrder = c(1,1)`, `model = "sGARCH"` | `vol="GARCH", p=1, q=1` |
| GJR-GARCH(1,1) | `model = "gjrGARCH"`, `garchOrder = c(1,1)` | `vol="GARCH", p=1, o=1, q=1` |
| EGARCH(1,1) | `model = "eGARCH"`, `garchOrder = c(1,1)` | `vol="EGARCH", p=1, o=1, q=1` |
| Distribution normale / Student | `distribution.model = "norm"` / `"std"` | `dist="normal"` / `dist="t"` |
| Moyenne constante, pas d'ARMA | `mean.model = list(armaOrder = c(0,0), include.mean = TRUE)` | `mean="Constant"` (par défaut) |

| Résultat | `R` | `Python` |
|---|---|---|
| Coefficients | `coef(fit)` — noms `alpha1`, `beta1`, `gamma1`... | `res.params` — noms `alpha[1]`, `beta[1]`, `gamma[1]`... |
| Volatilité conditionnelle $\widehat\sigma_t$ | `sigma(fit)` | `res.conditional_volatility` |
| Rendement ajusté $\widehat\mu_t$ | `fitted(fit)` | `res.params["mu"]` (constant, pas de série si `mean="Constant"`) |
| Résidus standardisés | `residuals(fit, standardize = TRUE)` | `res.std_resid` |
| AIC / BIC / log-vraisemblance | `infocriteria(fit)` | `res.aic`, `res.bic`, `res.loglikelihood` |
| Prévision | `ugarchforecast(fit, n.ahead = h)` | `res.forecast(horizon=h, reindex=False)` |
| Quantile de la loi des innovations (VaR) | `qdist("std", p, shape = coef(fit)["shape"])` | `res.model.distribution.ppf(p, [res.params["nu"]])` |

> **Convention de signe de l'asymétrie.** Le coefficient `gamma1` (`rugarch`)
> et `gamma[1]` (`arch`) mesurent tous deux l'effet de levier, mais leur
> **signe attendu diffère entre GJR et EGARCH**, et les deux packages ne
> normalisent pas nécessairement de manière identique. Ne concluez jamais sur
> le signe seul : relisez la définition du modèle (chapitre 3) avant
> d'interpréter.

> **La distribution `"std"` de `rugarch` est standardisée** (variance 1),
> exactement comme le `dist="t"` de `arch` : ce n'est **pas** un Student
> $t_\nu$ brut. `res.model.distribution.ppf(p, [nu])` renvoie directement le
> quantile de la loi standardisée utilisée dans l'estimation — pas besoin de
> reconstruire la mise à l'échelle $\sqrt{(\nu-2)/\nu}$ à la main, mais c'est
> ce que la fonction fait en interne.

---

## GARCH multivarié / DCC (chapitre 4)

**Il n'existe pas d'équivalent `Python` mûr et largement adopté à
`rmgarch`.** Les corrigés `Python` du TP4 utilisent un petit module maison,
`03-TP/dcc.py`, qui réestime **exactement** la procédure en deux étapes du
cours (Engle 2002) : $N$ GARCH univariés (`arch`) puis la dynamique de
corrélation par QMLE, codée à la main avec `scipy.optimize`.

| Opération | `R` (`rmgarch`) | `Python` (`03-TP/dcc.py`) |
|---|---|---|
| Spécifications univariées | `multispec(replicate(N, uspec))` | boucle interne à `DCCGARCH._fit_univariate()` |
| Spécifier le DCC | `dccspec(uspec, dccOrder = c(1,1), distribution = "mvnorm")` | `DCCGARCH(returns).fit(dcc_order=(1,1))` |
| CCC (cas emboîté) | `dccOrder = c(0,0)` | `.fit(dcc_order=(0,0))` |
| Paramètres $\theta_1,\theta_2$ | `coef(fit)["[Joint]dcca1"]`, `["[Joint]dccb1"]` | `.theta_` (tuple `(a, b)`) |
| Corrélations conditionnelles $\mathbf R_t$ | `rcor(fit)` | `.rcor()` — tableau `(T, N, N)` |
| Covariances conditionnelles $\mathbf H_t$ | `rcov(fit)` | `.rcov()` — tableau `(T, N, N)` |
| Une paire d'actifs | `rcor(fit)["CAC40", "DAX", ]` | `.rcor_pair("CAC40", "DAX")` — `pd.Series` indexée par date |
| Log-vraisemblance | `likelihood(fit)` | `.loglik_` |

C'est un choix pédagogique délibéré autant qu'une nécessité : coder soi-même
la récursion $Q_t = (1-\theta_1-\theta_2)\bar Q + \theta_1\varepsilon_{t-1}\varepsilon_{t-1}' + \theta_2 Q_{t-1}$
rend visible la décomposition $Q1L_T(\theta_V) + Q2L_T(\theta_R)$ du cours —
`rmgarch` fait la même chose, mais dans une boîte fermée.

---

## Graphiques

| Opération | `R` (`ggplot2`) | `Python` (`matplotlib`) |
|---|---|---|
| Plusieurs séries sur un graphique | `ggplot(df_long, aes(x, y, color = groupe)) + geom_line()` après `melt()` | boucle `for nom, s in dict.items(): ax.plot(s, label=nom)` puis `ax.legend()` |
| Thème | `theme_minimal()` | `plt.style.use("seaborn-v0_8-whitegrid")` (ou par défaut) |
| Deux graphiques empilés | `par(mfrow = c(2,1))` (base R) | `fig, ax = plt.subplots(2, 1, sharex=True)` |

---

## Données externes

Comme en cours, les fiches téléchargent leurs données **à la volée** — il n'y
a pas de fichiers versionnés dans `04-Data/` comme en M1. Une connexion
internet est donc nécessaire pour reproduire les corrigés, et les chiffres
exacts peuvent varier légèrement d'une session à l'autre.

| Source | `R` | `Python` |
|---|---|---|
| Yahoo Finance | `quantmod::getSymbols()` | `yfinance.download()` |

---

## Ce qui n'a pas d'équivalent direct

| | |
|---|---|
| `rmgarch` (DCC, BEKK...) | à reconstruire — voir `03-TP/dcc.py` |
| `FinTS::ArchTest` | `statsmodels.stats.diagnostic.het_arch` (même test, nom différent) |
| `rugarch::ugarchspec` / `ugarchfit` séparés | `arch_model(...).fit()` fait les deux d'un coup |
