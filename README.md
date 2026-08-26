# Économétrie financière — M2

**Université Paris 8 (M2 MBFA) et UPEC (M2 MASERATI, Créteil)**
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

## Un seul cours, deux rythmes

Il n'y a **qu'un seul cours** — un seul jeu de chapitres, de TD et de TP,
écrit au niveau de détail Paris 8. Il est donné dans deux universités, à
des rythmes différents :

| | Paris 8 (M2 MBFA) | Créteil (M2 MASERATI, UPEC) |
|---|---|---|
| Volume horaire | 36 h | 18 h |
| Séances | 12 × 3 × 50 min | 6 × 3 × 50 min |
| Évaluation | Projet 40 % + examen final 60 % | Aucune |

Le contenu s'adapte en séance, pas à l'avance : à Créteil, l'enseignant
raccourcit en direct selon le niveau du groupe plutôt que de suivre un
découpage figé. Le syllabus, lui, diffère réellement d'un site à l'autre
(volume horaire, modalités d'évaluation) — d'où deux fichiers distincts.

---

## Où trouver quoi

| Dossier | Contenu |
|---|---|
| `00-Syllabus/etudiant/` | Présentation générale, par site : plan, objectifs, évaluation |
| `01-Slides/etudiant/` | Les quatre chapitres du cours, en HTML |
| `02-TD/` | Les fiches de travaux dirigés — exercices sur papier |
| `03-TP/` | Les fiches de travaux sur machine (`R`) |
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

---

## Installation

`R` ≥ 4.2, avec au minimum les packages `quantmod`, `tidyverse`, `rugarch`,
`rmgarch`, `FinTS`, `moments`, `tseries`, `forecast`, `ggplot2`,
`gridExtra`, `reshape2`, `knitr`. Voir `install-packages.R`.

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

| | Paris 8 (M2 MBFA) | Créteil (M2 MASERATI, UPEC) |
|---|---|---|
| Modalité | Projet (40 %) + examen final (60 %) | Aucune |

Le détail du projet et de l'examen (Paris 8) est dans
`00-Syllabus/etudiant/syllabus-paris8.qmd`.

---

## Bibliographie

Engle (1982), Bollerslev (1986), Nelson (1991), Glosten, Jagannathan &
Runkle (1993), Engle & Kroner (1995), Engle & Sheppard (2001), Engle
(2002), Kupiec (1995), Christoffersen (1998). Les références précises
sont données au fil des chapitres.

---

## Licence et usage

Matériel pédagogique mis à disposition des étudiants des M2 MBFA
(Université Paris 8) et MASERATI (UPEC). Réutilisation à des fins
d'enseignement bienvenue, avec mention de la source — voir `LICENSE`
(CC BY-NC-SA 4.0).
