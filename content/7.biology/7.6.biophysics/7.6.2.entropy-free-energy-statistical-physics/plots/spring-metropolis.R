# Metropolis sampling of a bead in a harmonic trap, E(x) = k x^2 / 2 (k = 0.05 pN/nm, kBT = 4.28 pN nm).
set.seed(1)
k <- 0.05; kT <- 4.28
n <- 40000; step <- 12
x <- numeric(n); x[1] <- 40
for (i in 2:n) {
  y <- x[i - 1] + runif(1, -step, step)
  dE <- 0.5 * k * (y^2 - x[i - 1]^2)
  x[i] <- if (dE <= 0 || runif(1) < exp(-dE / kT)) y else x[i - 1]
}
xs <- x[-(1:1000)]
sig <- sqrt(kT / k)
op <- par(mfrow = c(1, 3))
plot(x[1:600], type = "l", xlab = "Monte Carlo step", ylab = "x / nm", main = "Markov chain")
hist(xs, breaks = 60, freq = FALSE, xlab = "x / nm", main = "Boltzmann distribution")
curve(dnorm(x, 0, sig), add = TRUE, col = "red", lwd = 2)
E <- 0.5 * k * xs^2 / kT
plot(cumsum(E) / seq_along(E), type = "l", log = "x", ylim = c(0, 1.2),
     xlab = "number of samples", ylab = "running <E> / kBT", main = "Equipartition")
abline(h = 0.5, lty = 2)
par(op)
cat("variance:", var(xs), " expected:", kT / k, "\n")
