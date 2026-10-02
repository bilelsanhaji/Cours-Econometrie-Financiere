# Économétrie financière — M2

**Université Paris 8 (M2 MBFA, parcours finance)**
B. Sanhaji

---

## De quoi il s'agit

Le cours applique à la finance les outils de l'économétrie des séries
temporelles : modéliser la moyenne conditionnelle des rendements (ARMA),
puis leur variance conditionnelle (ARCH/GARCH), puis les covariances et
corrélations conditionnelles entre plusieurs actifs (GARCH multivarié).

| | Chapitre | Ce que vous saurez faire |
|---|---|---|
| **1** | Données financières et faits stylisés | Calculer des rendements, caractériser leur distribution, reconnaître les faits stylisés |
| **2** | Processus ARMA | Identifier, estimer et valider un ARMA |
| **3** | Modèles ARCH et GARCH univariés | Tester l'effet ARCH, spécifier et estimer un GARCH, comparer les modèles asymétriques |
| **4** | GARCH multivarié | Estimer un DCC, interpréter des corrélations dynamiques, calculer et *backtester* une VaR de portefeuille |

À la fin du semestre, vous devez pouvoir spécifier, estimer et valider un
modèle de volatilité sur des données financières réelles, et en tirer une
mesure de risque.

---

## Organisation

**36 h, 12 séances de 3 × 50 min**, cours et applications sur `R` (ou
`Python`) intégrés dans la même séance.

---

## Où trouver quoi

| Dossier | Contenu |
|---|---|
| `00-Syllabus/etudiant/` | Présentation générale : plan, objectifs, évaluation |
| `01-Slides/etudiant/` | Les quatre chapitres du cours, en HTML |
| `02-TD/` | Les fiches de travaux dirigés — exercices sur papier |
| `03-TP/` | Les fiches de travaux sur machine (`R` ou `Python`, au choix) |
| `04-Data/` | Séries utilisées en TD et en TP |
| `05-Eval/` | Sujets d'examen des années passées, le cas échéant |

Les **corrigés** des TD et des TP sont déposés après chaque séance, dans
`02-TD/corriges/` et `03-TP/corriges/`.

Les chapitres se lisent dans un navigateur : ouvrez le fichier `.html`, il
fonctionne hors ligne. `Échap` donne la vue d'ensemble, `F` le plein écran.

---

## Récupérer le cours

```bash
git clone https://github.com/bilelsanhaji/Cours-Econometrie-Financiere.git
cd Cours-Econometrie-Financiere
```

Le dépôt est mis à jour au fil du semestre. Pour récupérer les ajouts :

```bash
git pull
```

Sans `git`, le bouton **Code → Download ZIP** de la page GitHub fait
l'affaire — mais il faudra le refaire à chaque mise à jour.

Une règle à retenir : **n'écrivez jamais dans les fichiers du dépôt**, sinon
`git pull` se bloquera. Créez un dossier `mon-travail/` et travaillez sur
des copies — `git` n'y touchera jamais.

`MISES-A-JOUR.md` détaille la procédure complète : cloner depuis RStudio ou
GitHub Desktop plutôt que le terminal, se débloquer quand `git pull` refuse
d'avancer, être prévenu des nouveaux dépôts. Et pourquoi *forker* le dépôt
n'est pas ce qu'il vous faut.

---

## Installation

Les travaux sur machine (`03-TP/`) se font au choix en `R` ou en `Python` —
voir `03-TP/README.md` et `03-TP/correspondance-R-python.md`.

| | À installer | Paquets |
|---|---|---|
| `R` | `R` ≥ 4.2 | `source("install-packages.R")` (`quantmod`, `tidyverse`, `rugarch`, `rmgarch`, `FinTS`, `moments`, `tseries`, `forecast`, `ggplot2`, `gridExtra`, `reshape2`, `knitr`) |
| `Python` | `Python` ≥ 3.10 | `pip install -r 03-TP/environnements/requirements.txt` (`arch`, `statsmodels`, `yfinance`, `pmdarima`...) |

Pour compiler les fiches en PDF, une distribution LaTeX est nécessaire :
`install.packages("tinytex"); tinytex::install_tinytex()`.

---

## Les données

Contrairement à d'autres cours où les séries sont versionnées dans le
dépôt, les chapitres et les TP téléchargent leurs données à la volée via
`quantmod::getSymbols` (CAC40, DAX, S&P500, actions individuelles selon
les fiches). Une connexion internet est donc nécessaire pour reproduire
les exemples — et les résultats peuvent varier légèrement d'une session
à l'autre si Yahoo Finance révise ses historiques.

---

## Évaluation

Projet (40 %) + examen final (60 %). Le détail est dans
`00-Syllabus/etudiant/syllabus-paris8.qmd`.

---

## Bibliographie

Engle (1982), Bollerslev (1986), Nelson (1991), Glosten, Jagannathan &
Runkle (1993), Engle & Kroner (1995), Engle & Sheppard (2001), Engle
(2002), Kupiec (1995), Christoffersen (1998). Les références précises
sont données au fil des chapitres.

---

## Licence et usage

Matériel pédagogique mis à disposition des étudiants du M2 MBFA
(Université Paris 8). Réutilisation à des fins d'enseignement bienvenue,
avec mention de la source — voir `LICENSE` (CC BY-NC-SA 4.0).
