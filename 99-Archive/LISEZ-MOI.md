# Archive

Rien n'a été supprimé lors de la restructuration. Ce dossier conserve les
sources qui ont servi à écrire les quatre chapitres (le chapitre 3 a
servi de pilote, validé en premier ; les chapitres 1, 2 et 4 ont suivi
le même patron une fois le pilote approuvé).

## Ce qui est ici

| Dossier | Contenu | Origine |
|---|---|---|
| `sources-originales/creteil/` | `EF_CH0.Rmd`/`EF_Syllabus.Rmd` (syllabus), `EF_CH1.Rmd` à `EF_CH3.Rmd` (chapitres), `EF_APP.Rmd` (applications, dont DCC), `App_GARCH/`, `App_DonneesFinancieres/`, `TD2025.R` | Dossier plat `M2-Econometrie-Financiere/` (matériel Créteil/UPEC) |
| `sources-originales/paris8/` | Syllabus (`CM M2 MBFA EF SYLLABUS.tex`), introduction (`chap0_intro.tex`), le chapitre « tout-en-un » historique (`CM M2 MBFA EF.tex`, en grande partie commenté au-delà des tests), ARMA/VARMA (`3-TS-ARMA/`), GARCH univarié (`4-GARCH/garch.tex`), GARCH multivarié (`EF_CH4_MGARCH/chap9_mgarch.tex`), plan de cours (`Plan Econo Fin.docx`) | Dossier `M2 EconoFi - 47/` (matériel Paris 8) |

## Ce qui n'est **pas** ici, et pourquoi

- **Les dossiers complets `M2-Econometrie-Financiere/` et `M2 EconoFi -
  47/` ne sont pas dupliqués.** Ils restent, intacts, à leur emplacement
  d'origine sur votre Drive — PDF compilés, caches `.quarto`/Rmd,
  dossiers `.Rproj.user`, dépôts `.git` locaux (`TDR/TD/`, `TDR/TD2025/`),
  historiques R (`.RData`, `.Rhistory`). Aucun intérêt à les recopier :
  ce sont des artefacts de compilation ou de configuration locale, pas
  des sources de contenu.
- **Aucune donnée nominative ou administrative** : notes d'étudiants
  (`Evaluation/*.xlsx`), copies d'examen scannées, dossiers de rendus
  d'étudiants (`Evaluation/100 Session 1/.../assignsubmission_file`).
  Conformément à votre choix, elles restent uniquement dans le dossier
  Paris 8 d'origine, hors de cette restructuration.
- **`Theoretical Exercises 4 - Solution Guide.pdf`** (dans `M2 EconoFi -
  47/`) n'a pas été repris : c'est un document tiers (Morten Nyboe Tabor,
  *Econometrics II*, Université de Copenhague, 2018), pas un document
  que vous avez écrit. Il reste à son emplacement d'origine ; les
  exercices de `02-TD/TD3-garch.qmd` ont été écrits indépendamment.
- **Les annales d'examen** (`Evaluation/annales corrigés/`, énoncés et
  corrigés types sans copies ni notes) n'ont pas non plus été reprises
  dans `05-Eval/` — à faire si vous le souhaitez, voir le README.

## Une incohérence corrigée au passage

Le chapitre 3 original (`sources-originales/creteil/EF_CH3.Rmd`) donne
la *News Impact Curve* du GJR-GARCH avec les deux branches ($\varepsilon_t
\leq 0$ / $\varepsilon_t > 0$) inversées par rapport à la définition de
l'indicatrice $D_{t-1}$ donnée juste au-dessus dans le même document.
Corrigé dans `01-Slides/CM3-garch.qmd`, avec une note à l'intention de
l'enseignant à cet endroit précis du fichier.

## Sur les deux versions du chapitre GARCH univarié

`sources-originales/creteil/EF_CH3.Rmd` et
`sources-originales/paris8/4-GARCH/garch.tex` couvrent le même
programme, dans le même ordre (Introduction, modèles univariés, tests,
estimation, leptokurticité) : le second est la source Beamer/LaTeX
d'origine, le premier en est une réécriture Rmd plus récente qui ajoute
une annexe de code R. Le chapitre 3 du nouveau dépôt part de cette
réécriture (`EF_CH3.Rmd`), pas de la version Beamer — voir le README
pour le détail de la démarche.

## Sur la partie VARMA du chapitre 2

`sources-originales/paris8/3-TS-ARMA/CM M2 MBFA EF BEAMER.tex` contient
un plan complet de séries temporelles et ARMA univarié (repris presque
intégralement dans `01-Slides/CM2-arma.qmd`), mais sa section VARMA
n'a jamais été rédigée : dans le fichier source, elle se limite à une
ligne de commentaire LaTeX (« ce qui est vrai en univarié se généralise
en multivarié ») suivie d'un plan de chapitres futurs entièrement mis en
commentaire. `CM2-arma.qmd` reflète cet état : une slide « Extension
multivariée : VAR(1) » construite à partir du seul contenu VAR/ADL
réellement rédigé ailleurs dans le fichier (non commenté), plutôt qu'un
développement VARMA complet qui n'existait pas dans la source. À
enrichir si vous souhaitez creuser cette extension pour Paris 8.

## Sur le chapitre 4 (GARCH multivarié)

`sources-originales/paris8/EF_CH4_MGARCH/chap9_mgarch.tex` est une
source anglophone complète et déjà bien structurée (VEC, BEKK, CCC,
DCC, estimation en deux étapes, *variance targeting*) : traduite et
adaptée dans `01-Slides/CM4-mgarch.qmd` sans ajout de contenu théorique
nouveau. Sa toute dernière section (tests de non-linéarité pour BEKK,
travail de recherche non finalisé, entièrement en commentaire dans le
fichier source) n'a pas été reprise : hors du niveau attendu pour ce
cours de M2.
