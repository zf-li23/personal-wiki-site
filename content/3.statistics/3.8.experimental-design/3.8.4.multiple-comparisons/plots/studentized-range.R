# Densities of the studentized range distribution with 16 degrees of freedom for k = 2, 3, 4, 6.
# R has ptukey and qtukey but no density, so the density is a numerical derivative of ptukey.
nu <- 16
q <- seq(0.01, 7, length.out = 400)
h <- 1e-4
ks <- c(2, 3, 4, 6)
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")
plot(NA, xlim = c(0, 7), ylim = c(0, 0.75), xlab = "q", ylab = "density",
     main = "Studentized range distribution, nu = 16")
for (i in seq_along(ks)) {
  dens <- (ptukey(q + h, ks[i], nu) - ptukey(q - h, ks[i], nu)) / (2 * h)
  lines(q, dens, col = cols[i], lwd = 2)
  abline(v = qtukey(0.95, ks[i], nu), col = cols[i], lty = 3)
}
legend("topright", col = cols, lwd = 2, bty = "n",
       legend = sprintf("k = %d, q(0.05) = %.2f", ks, qtukey(0.95, ks, nu)))
