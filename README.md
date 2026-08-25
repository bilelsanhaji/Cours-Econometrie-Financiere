# Économétrie Financière — M2

**Paris 8 (M2 MBFA, 36 h) et UPEC/Créteil (M2 MASERATI, 18 h)**
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
| **2** | Processus ARMA (et VARMA à Paris 8) | Identifier, estimer et valider un ARMA |
| **3** | Modèles ARCH et GARCH univariés | Tester l'effet ARCH, spécifier et estimer un GARCH, comparer les modèles asymétriques |
| **4** | GARCH multivarié | Estimer un DCC, interpréter des corrélations dynamiques |

---

## Un seul cours, deux rythmes

Il n'y a **qu'un seul cours** — un seul jeu de chapitres, de TD et de
TP, écrit au niveau de détail Paris 8 (la version complète). Il est
donné dans deux universités, à des rythmes très différents :

| | Paris 8 (M2 MBFA) | Créteil (M2 MASERATI, UPEC) |
|---|---|---|
| Volume horaire | 36 h | 18 h |
| Séances | 12 × 3 h | 6 × 3 h |
| Évaluation | Projet 40 % + examen final 60 % | Aucune |

Pour Paris 8, `06-Enseignant/deroule-paris8.qmd` donne une correspondance
précise entre plages de slides et séances sur les 12 séances. Pour
Créteil, il n'y a pas de découpage pré-établi séance par séance : c'est
l'enseignant qui raccourcit en direct selon le niveau du groupe —
`06-Enseignant/deroule-creteil.qmd` donne des repères (ce qui se coupe
en premier, ce qui ne se compresse pas) plutôt qu'un script figé. Le
syllabus, en revanche, diffère réellement d'un site à l'autre (volume
horaire, modalités d'évaluation) — d'où deux fichiers dans
`00-Syllabus/`.

---

## Où trouver quoi

| Dossier | Contenu |
|---|---|
| `00-Syllabus/` | `syllabus-paris8.qmd`, `syllabus-creteil.qmd` — présentation générale, par site |
| `01-Slides/` | Les chapitres du cours (niveau Paris 8), en Quarto/`revealjs` |
| `02-TD/` | Fiches de travaux dirigés — exercices sur papier |
| `03-TP/` | Fiches de travaux sur machine (`R`) |
| `04-Data/` | Séries utilisées en TD et en TP |
| `05-Eval/` | Sujets d'examen des années passées *(à compléter — voir note ci-dessous)* |
| `06-Enseignant/` | Déroulés des séances, un par site |

Les **corrigés** des TD et des TP sont dans `02-TD/corriges/` et
`03-TP/corriges/`.

Les chapitres se lisent dans un navigateur : `quarto render
01-Slides/CM3-garch.qmd`, puis ouvrez le `.html` produit. `Échap` donne
la vue d'ensemble, `F` le plein écran.

---

## État d'avancement

Ce dossier a été réorganisé pour prendre la même forme que le cours de
Séries Temporelles (M1 MBFA) — même arborescence, même thème, même usage
de Quarto/`revealjs`, mêmes conventions de nommage. **Les quatre
chapitres sont désormais convertis.** Le chapitre 3 (ARCH/GARCH
univariés) a servi de pilote et a été validé en premier ; les chapitres
1, 2 et 4 suivent exactement le même patron (CM théorique sans code,
TD sur papier, TP avec corrigé `R` complet).

- ✅ Squelette du dépôt (`00` à `06` + `99`), thème, configuration Quarto
- ✅ Syllabus des deux sites
- ✅ Chapitre 1 : `CM1-donnees-faits-stylises.qmd`, `TD1-*.qmd`, `TP1-*.qmd`, corrigés
- ✅ Chapitre 2 : `CM2-arma.qmd`, `TD2-arma.qmd`, `TP2-arma.qmd`, corrigés
- ✅ Chapitre 3 : `CM3-garch.qmd`, `TD3-garch.qmd`, `TP3-garch.qmd`, corrigés *(pilote)*
- ✅ Chapitre 4 : `CM4-mgarch.qmd`, `TD4-mgarch.qmd`, `TP4-mgarch.qmd`, corrigés
- ✅ Déroulé détaillé (plages de slides par séance) pour Paris 8 ; guide léger (pas de découpage figé) pour Créteil
- ⬜ `04-Data/` — jeux de données versionnés (voir note)
- ⬜ `05-Eval/` — annales (aucune donnée nominative n'a été reprise, voir note)

**Depuis la version pilote** : le chapitre 4 s'est enrichi d'une partie
« VaR de portefeuille et *backtesting* » (test de Kupiec, aperçu de
Christoffersen — `CM4-mgarch.qmd`, désormais 29 slides au lieu de 25),
avec l'exercice associé dans `TD4-mgarch.qmd` (exercice 6) et son
prolongement appliqué dans `TP4-mgarch.qmd`/son corrigé (exercice 6) —
un contenu réellement nouveau (pas dans les sources originales),
justifié par le volume horaire de Paris 8 (36 h) et le niveau attendu
d'un cours de spécialité.

**À valider avant la première utilisation en séance** : ce dépôt n'a pu
être vérifié que structurellement (voir la note « Sur la vérification »
ci-dessous) — un rendu `quarto render` complet, chapitre par chapitre,
reste la première chose à faire une fois `quarto`/`R` disponibles.

Les sources originales — Paris 8 (`M2 EconoFi - 47/`) et Créteil (fichiers
`EF_*` à plat) — sont intactes dans `99-Archive/sources-originales/`. Voir
`99-Archive/LISEZ-MOI.md` pour le détail de ce qui a été repris, écarté,
ou laissé de côté.

**Note sur les données** : tous les chapitres (CAC40 au chapitre 3,
INTC/AAPL/S&P500 au chapitre 1, AAPL au chapitre 2, CAC40/DAX/S&P500 au
chapitre 4) téléchargent leurs données à la volée via
`quantmod::getSymbols`, comme dans les sources originales, plutôt que de
les verser dans `04-Data/` — à l'inverse de la convention du cours de
Séries Temporelles. Un renforcement possible mais non fait : figer ces
séries en CSV dans `04-Data/` rendrait le cours reproductible hors ligne
(et insensible aux révisions de données de Yahoo Finance), comme l'autre
cours.

**Note sur la vérification** : aucun environnement `Quarto`/`R` n'était
disponible lors de la construction de ce dépôt. Chaque fichier `.qmd` a
été vérifié structurellement (YAML, équilibre des `$`/`:::`/`\begin`-`\end`)
et passé au travers d'un parseur `pandoc` — aucune erreur, seulement les
avertissements attendus sur le rendu TeX du fichier `pandoc` (Quarto,
avec `html-math-method: mathjax`, gère les maths différemment). Cela
**ne remplace pas** un rendu `quarto render` réel : c'est la première
vérification à faire chapitre par chapitre avant la première séance,
en particulier pour le code `R` des corrigés de TP (jamais exécuté).

**Note sur `05-Eval/`** : à la demande de l'enseignant, aucune donnée
nominative (notes, copies scannées, rendus d'étudiants) n'a été reprise
dans cette restructuration — ces éléments restent, non touchés, dans le
dossier Paris 8 d'origine. Si vous souhaitez reprendre les annales
d'examen (énoncés et corrigés types, sans copies ni notes), elles sont
dans `99-Archive/sources-originales/paris8/Evaluation/annales corrigés/`.

---

## Installation

`R` ≥ 4.2, avec au minimum les packages `quantmod`, `tidyverse`,
`rugarch`, `rmgarch`, `FinTS`, `moments`, `tseries`, `forecast`,
`ggplot2`, `gridExtra`, `reshape2`, `knitr`. Voir `install-packages.R`.

Pour compiler les fiches en PDF, une distribution LaTeX est nécessaire :
`install.packages("tinytex"); tinytex::install_tinytex()`.

---

## Dépôt GitHub

Ce dépôt est destiné à être public sur GitHub. Le dossier
`99-Archive/sources-originales/` (matériaux bruts pré-conversion,
Rmd/tex non retravaillés pour la publication) est exclu du suivi `git`
via `.gitignore` — il reste disponible en local et dans votre Drive,
mais n'est pas poussé sur GitHub. `99-Archive/LISEZ-MOI.md`, lui, est
suivi : c'est la documentation de ce qui a été repris des sources et
pourquoi.

## Licence et usage

Matériel pédagogique mis à disposition des étudiants des M2 MBFA
(Université Paris 8) et MASERATI (UPEC), et publié publiquement sur
GitHub. Réutilisation à des fins d'enseignement bienvenue, avec mention
de la source — voir `LICENSE` (CC BY-NC-SA 4.0).
