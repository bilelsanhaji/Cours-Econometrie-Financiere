# Mémo terminal

Depuis la racine du dépôt (`M2-Econometrie-Financiere/`).

## Mettre à jour le dépôt

```bash
git pull
```

## Cours (`01-Slides/`) — HTML puis PDF

Le HTML est la version de référence ; le PDF est un instantané imprimé
(`decktape`), pas un format généré nativement par Quarto ici (les blocs
`definition`/`retenir`/`piège` sont stylés en CSS, pas en LaTeX).

```bash
# Setup une seule fois
npm install -g decktape

# Un chapitre : html puis pdf
quarto render 01-Slides/etudiant/CM1-donnees-faits-stylises.qmd
cd 01-Slides/etudiant
decktape reveal --size 1280x760 "file://$(pwd)/CM1-donnees-faits-stylises.html" CM1-donnees-faits-stylises.pdf
cd -

# Les 4 chapitres d'un coup
for f in CM1-donnees-faits-stylises CM2-arma CM3-garch CM4-mgarch; do
  quarto render "01-Slides/etudiant/$f.qmd"
  (cd 01-Slides/etudiant && decktape reveal --size 1280x760 "file://$(pwd)/$f.html" "$f.pdf")
done
```

Profil tableau blanc (annotation en séance, à garder pour soi, pas à
distribuer) :

```bash
quarto render 01-Slides/CM3-garch.qmd --profile tableau
```

Graphiques absents dans le `.html` → ouvrir le fichier dans un vrai
navigateur (pas Quick Look, pas l'aperçu Google Drive) : reveal.js charge
les images en JS (`data-src`), qui ne s'exécute pas dans ces aperçus.

## TD / TP (`02-TD/`, `03-TP/`) — PDF direct

Ces fiches sont en `format: pdf` (LaTeX/tinytex) : pas besoin de decktape.

```bash
quarto render 03-TP/TP1-donnees-faits-stylises.qmd
quarto render 02-TD/TD1-donnees-faits-stylises.qmd
```

## Rendre tout le dépôt

```bash
quarto render
```

## Installer/mettre à jour les packages

```bash
# R
Rscript install-packages.R

# Python
pip install -r 03-TP/environnements/requirements.txt

# PDF (LaTeX), une fois
Rscript -e 'tinytex::install_tinytex()'
```

## Publier sur GitHub

Double-cliquer `publier-Cours-EconoFinanciere.command` (vérifie qu'aucun
contenu enseignant ne part avant de commit + push). Pour inclure un
corrigé malgré le `.gitignore` :

```bash
git add -f 02-TD/corriges/TD1-donnees-faits-stylises-corrige.qmd
```
