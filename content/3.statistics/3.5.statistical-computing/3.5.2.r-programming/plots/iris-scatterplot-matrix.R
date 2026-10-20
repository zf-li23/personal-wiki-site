# Scatterplot matrix of the iris measurements, colored by species, with correlations in the lower panels.
panel_cor <- function(x, y, ...) {
  usr <- par("usr"); on.exit(par(usr = usr))
  par(usr = c(0, 1, 0, 1))
  text(0.5, 0.5, sprintf("R = %.2f", cor(x, y)))
}
species <- as.integer(iris$Species)       # one color and symbol per observation, by species
pairs(iris[, 1:4], col = species, pch = c(1, 2, 3)[species],
      lower.panel = panel_cor, oma = c(6, 3, 3, 3))
par(xpd = TRUE)                           # allow the legend outside the plot region
legend("bottom", horiz = TRUE, bty = "n", col = 1:3, pch = 1:3, legend = levels(iris$Species))
