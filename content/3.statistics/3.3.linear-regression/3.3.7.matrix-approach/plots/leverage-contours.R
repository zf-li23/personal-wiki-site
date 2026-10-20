# Leverage in a regression with two predictors: contours of constant h_ii are Mahalanobis ellipses.
library(MASS)
set.seed(0)
n <- 60
P <- mvrnorm(n, mu = c(0, 0), Sigma = matrix(c(1, 0.8, 0.8, 1), 2))
P[1, ] <- c(1.3, -1.2)

h <- hat(P, intercept = TRUE)   # diagonal of the hat matrix; equals hatvalues() of any lm on P
xbar <- colMeans(P)
Sinv <- solve(cov(P))
g <- seq(-3.2, 3.2, length.out = 300)
lev <- outer(g, g, function(a, b) {
  d <- cbind(a - xbar[1], b - xbar[2])
  1 / n + rowSums((d %*% Sinv) * d) / (n - 1)   # 1/n + Mahalanobis D^2 / (n - 1)
})

pal <- hcl.colors(100, "viridis")
cols <- pal[cut(h, 100, labels = FALSE)]
contour(g, g, lev, levels = c(0.05, 0.1, 0.15, 0.2, 0.3), labels = paste("h =", c(0.05, 0.1, 0.15, 0.2, 0.3)),
        col = "steelblue", asp = 1, xlab = "X_1", ylab = "X_2",
        main = "h_ii = 1/n + D^2/(n - 1): the marked point is not extreme\nin X_1 or X_2 alone, but it has the largest leverage",
        cex.main = 0.85)
points(P, pch = 19, col = cols)
text(P[1, 1] + 0.3, P[1, 2] - 0.5, sprintf("h = %.2f", h[1]), col = "firebrick", adj = 0)
arrows(P[1, 1] + 0.28, P[1, 2] - 0.42, P[1, 1] + 0.05, P[1, 2] - 0.05, length = 0.08, col = "firebrick")
