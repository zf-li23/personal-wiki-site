# Scatter plot matrix of a simulated four-variable data set with two groups (histograms on the diagonal).
library(MASS)

set.seed(0)
C <- matrix(c(1.0, 0.9, 0.2, 0.0,
              0.9, 1.0, 0.2, 0.0,
              0.2, 0.2, 1.0, -0.85,
              0.0, 0.0, -0.85, 1.0), 4, 4, byrow = TRUE)
A <- mvrnorm(100, mu = c(0, 0, 0, 0), Sigma = C)
B <- mvrnorm(100, mu = c(0.9, -0.9, 0.8, 0.8), Sigma = C)
X <- rbind(A, B)
colnames(X) <- paste0("X", 1:4)
group <- factor(rep(c("group A", "group B"), each = 100))
pal <- c("steelblue", "darkorange")

# Overlaid group histograms for the diagonal panels.
panel_hist <- function(x, ...) {
  usr <- par("usr")
  on.exit(par(usr = usr))
  breaks <- pretty(range(x), 20)
  ha <- hist(x[group == "group A"], breaks = breaks, plot = FALSE)
  hb <- hist(x[group == "group B"], breaks = breaks, plot = FALSE)
  par(usr = c(usr[1:2], 0, 1.1 * max(ha$counts, hb$counts)))
  nb <- length(breaks)
  rect(breaks[-nb], 0, breaks[-1], ha$counts, col = adjustcolor(pal[1], 0.5), border = NA)
  rect(breaks[-nb], 0, breaks[-1], hb$counts, col = adjustcolor(pal[2], 0.5), border = NA)
}

pairs(X, col = adjustcolor(pal[group], 0.6), pch = 19, cex = 0.4,
      diag.panel = panel_hist, oma = c(3, 3, 6, 3))
par(xpd = NA)
legend(grconvertX(0.5, "ndc", "user"), grconvertY(0.99, "ndc", "user"),
       xjust = 0.5, yjust = 1, horiz = TRUE, bty = "n",
       legend = levels(group), col = pal, pch = 19)
