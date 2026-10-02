# Suivre les mises à jour du cours

Le dépôt bouge pendant tout le semestre : chapitres corrigés, fiches de TD
et de TP ajoutées, corrigés déposés après chaque séance. Télécharger le ZIP
à chaque fois marche, mais vous repartez d'un dossier vide et vous perdez
votre travail en route.

**Le principe : vous copiez le dépôt une seule fois, puis une commande
suffit pour récupérer tout ce qui a changé depuis.** Cette copie s'appelle
un *clone*, et la commande de mise à jour est `git pull`.

---

## « Je peux forker le dépôt ? »

Techniquement oui, mais ce n'est pas fait pour ça, et ça vous ajoute du
travail plutôt que de vous en enlever.

Un **fork** est une copie du dépôt sur *votre* compte GitHub. Il sert à
proposer des modifications au dépôt d'origine — corriger une coquille,
ajouter du code. C'est le geste de quelqu'un qui veut **écrire** dans le
projet.

Or un fork ne se met pas à jour tout seul. Si vous forkez puis clonez votre
fork, `git pull` ira chercher les nouveautés… sur votre fork, qui n'en a
aucune. Vous devriez d'abord synchroniser le fork depuis GitHub (bouton
**Sync fork**), *puis* faire `git pull`. Deux gestes au lieu d'un, pour un
résultat identique.

**Ce qu'il vous faut, c'est un clone du dépôt d'origine.** Vous n'avez pas
besoin de compte GitHub, et vous n'avez rien à pousser : le dépôt est
public et vous êtes en lecture seule.

---

## Récupérer le cours (une seule fois)

Trois façons de faire. Elles donnent exactement le même résultat, choisissez
celle qui vous parle — l'adresse du dépôt est la même dans les trois cas :

```
https://github.com/bilelsanhaji/Cours-Econometrie-Financiere.git
```

### Avec RStudio

Vous l'avez déjà installé pour les TP, et le dépôt contient un projet
RStudio (`Cours-Econometrie-Financiere.Rproj`) — c'est la voie la plus
simple si vous travaillez en `R`.

1. **File → New Project… → Version Control → Git**
2. *Repository URL* : collez l'adresse ci-dessus
3. *Create project as subdirectory of* : choisissez où le ranger
   (vos documents, par exemple — **pas** un dossier synchronisé par
   Dropbox, iCloud ou OneDrive, qui se querellent avec `git`)
4. **Create Project**

Si l'entrée *Git* n'apparaît pas, c'est que `git` n'est pas installé —
voir plus bas.

### Avec GitHub Desktop

Une application graphique, sans ligne de commande : à télécharger sur
[desktop.github.com](https://desktop.github.com).

1. **File → Clone repository… → URL**
2. Collez l'adresse, choisissez le dossier de destination
3. **Clone**

### Avec le terminal

```bash
git clone https://github.com/bilelsanhaji/Cours-Econometrie-Financiere.git
cd Cours-Econometrie-Financiere
```

Si la commande `git` est inconnue :

| | |
|---|---|
| **macOS** | `xcode-select --install`, ou `brew install git` |
| **Windows** | [git-scm.com/download/win](https://git-scm.com/download/win) — ouvre ensuite « Git Bash » |
| **Linux** | `sudo apt install git` |

---

## Se mettre à jour (à chaque séance)

| | |
|---|---|
| **RStudio** | Onglet **Git** (en haut à droite) → la flèche bleue vers le bas, **Pull** |
| **GitHub Desktop** | **Fetch origin**, puis **Pull origin** s'il y a du nouveau |
| **Terminal** | `git pull`, depuis le dossier du cours |

C'est tout. Seuls les fichiers modifiés sont téléchargés, pas le dépôt
entier — c'est quelques secondes, même sur une connexion médiocre.

Pour voir ce qui vient d'arriver :

```bash
git log --oneline -10
```

---

## La règle d'or : ne modifiez pas les fichiers du dépôt

C'est le seul vrai piège, et il n'a rien de technique.

`git pull` remplace les fichiers du cours par leur nouvelle version. Si
vous avez écrit vos réponses **dans** `03-TP/TP2-arma.qmd`, `git` refuse
de continuer plutôt que d'écraser votre travail — et vous voilà bloqué.

**Travaillez toujours sur une copie, dans un dossier à vous.** Créez à la
racine du dépôt un dossier `mon-travail/` :

```
Cours-Econometrie-Financiere/
├── 03-TP/
│   └── TP2-arma.qmd          ← le sujet, jamais touché
└── mon-travail/
    └── TP2-mes-reponses.R    ← votre fichier
```

Les fichiers que vous créez vous-même ne sont pas suivis par `git` : il ne
les touchera jamais, ni pour les modifier, ni pour les supprimer. Vous
pouvez faire `git pull` autant de fois que vous voulez, votre travail ne
risque rien.

---

## Si `git pull` refuse d'avancer

Le message ressemble à :

```
error: Your local changes to the following files would be overwritten by merge:
        03-TP/TP2-arma.qmd
```

Traduction : vous avez modifié un fichier du cours, et la mise à jour
toucherait ce même fichier. Pour vous en sortir :

1. **Mettez votre version à l'abri** — copiez le fichier dans
   `mon-travail/` sous un autre nom, par le Finder ou l'Explorateur.
2. **Rendez au dépôt sa version d'origine**, puis mettez à jour :

```bash
git restore 03-TP/TP2-arma.qmd
git pull
```

Avec une version ancienne de `git`, `git restore` n'existe pas ; la
commande équivalente est `git checkout -- 03-TP/TP2-arma.qmd`.

Pour tout remettre d'aplomb d'un coup, quels que soient les fichiers
concernés — **après** avoir mis vos fichiers modifiés à l'abri, car cette
commande efface toutes vos modifications sur les fichiers du cours :

```bash
git restore .
git pull
```

En dernier recours, supprimez le dossier et reclonez : vous ne perdez que
ce qui s'y trouvait, d'où l'intérêt de garder votre travail dans
`mon-travail/` — ou mieux, ailleurs sur votre machine.

---

## Être prévenu des nouveautés

Sur la page GitHub du dépôt, bouton **Watch** (en haut à droite) →
**All Activity**. GitHub vous envoie un courriel à chaque dépôt de fichier.
Il faut un compte GitHub, gratuit.

Sinon, l'onglet **Commits** de la page du dépôt liste les derniers ajouts,
avec leur date, sans rien installer ni créer.

---

## Et si je ne veux rien installer ?

Le bouton **Code → Download ZIP** de la page GitHub reste disponible. C'est
la solution de repli : un dossier neuf à chaque fois, à retélécharger
intégralement pour la moindre mise à jour, et à vous de ne pas confondre
les versions. Pour un semestre entier, l'installation de `git` est vite
rentabilisée.
