# Les travaux sur machine

**`R` ou `Python`, au choix.** Le choix est libre, réversible en cours de semestre, et sans aucune incidence sur la notation. Chaque fiche a un corrigé dans les deux langages.

------------------------------------------------------------------------

## Les fiches

| Fiche | Chapitre | Contenu |
|------------------------|------------------------|------------------------|
| `TP1-donnees-faits-stylises` | 1 | Rendements, statistiques descriptives, faits stylisés |
| `TP2-arma` | 2 | Identification et estimation d'un ARMA sur données réelles |
| `TP3-garch` | 3 | ARCH, GARCH, GJR, EGARCH, VaR et backtesting |
| `TP4-mgarch` | 4 | DCC-GARCH sur un petit portefeuille, VaR de portefeuille |

Les fiches préparent directement les parties correspondantes du **projet** (Paris 8) : TP1 → faits stylisés, TP2 → ARMA, TP3 → GARCH univarié, TP4 → portefeuille.

Les **corrigés** sont dans `corriges/`, déposés après chaque séance, en `R` et en `Python`.

------------------------------------------------------------------------

## Charger les données

Contrairement au cours de séries temporelles (M1), les données ne sont **pas** versionnées dans le dépôt : chaque fiche télécharge ses prix à la volée sur Yahoo Finance.

### `R`

``` r
library(quantmod)
FCHI <- getSymbols("^FCHI", from = "2018-01-01", to = "2023-12-31",
                    src = "yahoo", auto.assign = FALSE)
```

### `Python`

``` python
import yfinance as yf
FCHI = yf.download("^FCHI", start="2018-01-01", end="2023-12-31", auto_adjust=True)
```

**Une connexion internet est donc nécessaire** pour reproduire les corrigés, et les chiffres exacts peuvent varier légèrement d'une session à l'autre si Yahoo Finance révise son historique — les commentaires des corrigés sont rédigés en conséquence ("généralement", "on observe en général...").

------------------------------------------------------------------------

## Passer d'un langage à l'autre

`correspondance-R-python.md` donne, fonction par fonction, l'équivalence pour tout le programme : ARMA, tests de diagnostic, GARCH univarié, DCC-GARCH.

Il signale en particulier :

-   pour le GARCH univarié, `rugarch` sépare spécification (`ugarchspec`) et estimation (`ugarchfit`) là où `arch_model(...).fit()` fait les deux d'un coup ;
-   **il n'existe pas d'équivalent `Python` mûr à `rmgarch`.** Le TP4 s'appuie sur un petit module maison, `03-TP/dcc.py`, qui réestime la procédure en deux étapes du chapitre 4 (Engle 2002) plutôt que de s'en remettre à un package tiers ;
-   les conventions de signe du coefficient d'asymétrie (`gamma1` / `gamma[1]`) ne sont pas forcément identiques entre `rugarch` et `arch` selon le modèle (GJR vs EGARCH) — toujours vérifier contre la définition du modèle avant d'interpréter un signe.

------------------------------------------------------------------------

## Environnement

|          |                                            |
|----------|--------------------------------------------|
| `R`      | `install-packages.R`, à la racine du dépôt |
| `Python` | `environnements/requirements.txt`          |

``` bash
pip install -r 03-TP/environnements/requirements.txt
```

ou

``` bash
pip3 install -r 03-TP/environnements/requirements.txt
```

## Travailler sur notebook

Les corrigés `Python` sont des fichiers `.qmd`. Ils s'ouvrent tels quels dans **VS Code** et **Positron**, qui exécutent les cellules directement.

Pour un vrai `.ipynb` — sur Google Colab, par exemple :

``` bash
# depuis la racine du dépôt
quarto convert 03-TP/corriges/TP3-garch-python-corrige.qmd
```

Le chemin doit être celui vu depuis l'endroit où vous lancez la commande. Le notebook est écrit à côté du `.qmd`.

Si `quarto convert` échoue, `jupytext` fait la même chose :

``` bash
pip install jupytext
jupytext --to ipynb 03-TP/corriges/TP3-garch-python-corrige.qmd
```