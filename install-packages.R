# Installation des packages nécessaires au cours
# Économétrie Financière — M2 (Paris 8 / Créteil)

packages <- c(
  "quantmod",      # import de données financières (Yahoo Finance)
  "tidyverse",     # manipulation de données, ggplot2
  "rugarch",       # modèles GARCH univariés
  "rmgarch",       # modèles GARCH multivariés (DCC, BEKK...)
  "FinTS",         # test ARCH (ArchTest)
  "moments",       # skewness, kurtosis
  "tseries",       # tests (Jarque-Bera, ADF, KPSS...)
  "forecast",      # ARMA (auto.arima)
  "gridExtra",     # mise en page de graphiques
  "reshape2",      # melt() pour ggplot
  "knitr",         # tableaux, rendu Quarto/R Markdown
  "kableExtra"     # mise en forme de tableaux
)

installes <- rownames(installed.packages())
a_installer <- setdiff(packages, installes)

if (length(a_installer) > 0) {
  install.packages(a_installer)
} else {
  message("Tous les packages sont déjà installés.")
}
