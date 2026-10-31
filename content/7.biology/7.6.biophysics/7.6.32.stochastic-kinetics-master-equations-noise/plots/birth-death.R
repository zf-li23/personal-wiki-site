# Birth-death process of mRNA (k = 20, gamma = 1) simulated with the Gillespie algorithm.
set.seed(1)
k <- 20; g <- 1
gillespie <- function(m0, tmax) {
  t <- 0; m <- m0; ts <- t; ms <- m
  while (t < tmax) {
    a <- c(k, g * m); a0 <- sum(a)
    t <- t + rexp(1, a0)
    m <- m + if (runif(1) < a[1] / a0) 1 else -1
    ts <- c(ts, t); ms <- c(ms, m)
  }
  list(t = ts, m = ms)
}
# relaxation from m = 0 against the exact mean k (1 - exp(-t))
plot(NULL, xlim = c(0, 5), ylim = c(0, 35), xlab = "gamma t", ylab = "m")
for (i in 1:5) { s <- gillespie(0, 5); lines(s$t, s$m, type = "s", col = "orange") }
curve(k * (1 - exp(-x)), add = TRUE, lwd = 2)
# time-weighted stationary distribution against Poisson(k / gamma)
s <- gillespie(20, 2000)
w <- tapply(diff(s$t), head(s$m, -1), sum); w <- w / sum(w)
n <- as.integer(names(w))
barplot(w, names.arg = n, xlab = "m", ylab = "probability")
points(seq_along(n) * 1.2 - 0.5, dpois(n, k / g), pch = 16)
mu <- sum(n * w); cat("Fano factor:", (sum(n^2 * w) - mu^2) / mu, "\n")
