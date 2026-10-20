# Sample canonical variates for simulated data with two sets of variables (p = 2, q = 3).
set.seed(0)
n <- 300
z <- matrix(rnorm(n * 2), n, 2)
X1 <- cbind(z[, 1] + 0.4 * rnorm(n), 0.6 * z[, 2] + 0.9 * rnorm(n))
X2 <- cbind(z[, 1] + 0.3 * z[, 2] + 0.5 * rnorm(n),
            0.7 * z[, 2] + 0.8 * rnorm(n),
            rnorm(n))

cc <- cancor(X1, X2)
print(cc$cor)  # sample canonical correlations
# cancor scales the variates to unit sum of squares; multiply by sqrt(n - 1) for unit variance.
U <- scale(X1, center = cc$xcenter, scale = FALSE) %*% cc$xcoef * sqrt(n - 1)
V <- scale(X2, center = cc$ycenter, scale = FALSE) %*% cc$ycoef[, 1:2] * sqrt(n - 1)

lim <- range(U, V)
cols <- c("steelblue", "darkorange")
par(mfrow = c(1, 2))
for (k in 1:2) {
  plot(U[, k], V[, k], pch = 19, cex = 0.5, col = adjustcolor(cols[k], 0.6), asp = 1,
       xlim = lim, ylim = lim, xlab = paste0("U_", k), ylab = paste0("V_", k),
       main = sprintf("pair %d: sample canonical correlation = %.2f", k, cc$cor[k]), cex.main = 0.9)
  grid()
}
