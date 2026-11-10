# Sample paths of the uniform empirical process, and the simulated null distribution of sqrt(n) D_n
# (n = 20) against the Kolmogorov density.
set.seed(0)
op <- par(mfrow = c(1, 2))
n <- 1000
plot(NULL, xlim = c(0, 1), ylim = c(-2, 2), xlab = "t", ylab = "sqrt(n) (Fn(t) - t)")
for (k in 1:5) {
  u <- c(0, sort(runif(n)), 1)
  lines(u, sqrt(n) * (c(0, (1:n) / n, 1) - u), type = "s", col = k)
}
abline(h = 0)
n <- 20
d <- replicate(20000, ks.test(runif(n), "punif", exact = TRUE)$statistic)
hist(sqrt(n) * d, breaks = 60, freq = FALSE, main = "", xlab = "x")
kolmogorov_cdf <- function(x) 1 - 2 * sum((-1)^(0:99) * exp(-2 * (1:100)^2 * x^2))
s <- seq(0.3, 2.2, by = 0.01)
dens <- diff(sapply(s, kolmogorov_cdf)) / 0.01
lines(s[-1], dens, col = "firebrick", lwd = 2)
par(op)
