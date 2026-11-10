# Rerandomization: distribution of the difference in means and variance reduction versus theory
set.seed(0)
n <- 100; n_t <- 50; k <- 4
x <- matrix(rnorm(n * k), n, k)
y0 <- drop(x %*% rep(0.5, k)) + rnorm(n)
y1 <- y0 + 1
s_inv <- solve(cov(x))

draws <- 40000
sim <- replicate(draws, {
  w <- sample(rep(c(TRUE, FALSE), c(n_t, n - n_t)))
  diff <- colMeans(x[w, ]) - colMeans(x[!w, ])
  c(m = n_t * (n - n_t) / n * drop(t(diff) %*% s_inv %*% diff),
    tau = mean(y1[w]) - mean(y0[!w]))
})
m_stat <- sim["m", ]; tau_hat <- sim["tau", ]
r2 <- summary(lm(y0 ~ x))$r.squared

keep <- m_stat <= qchisq(0.1, k)
op <- par(mfrow = c(1, 2))
hist(tau_hat, breaks = 60, freq = FALSE, col = rgb(0, 0, 1, 0.4), border = NA,
     xlab = "difference in means", main = "complete vs rerandomization")
hist(tau_hat[keep], breaks = 60, freq = FALSE, col = rgb(1, 0.5, 0, 0.5), border = NA, add = TRUE)
abline(v = 1, lty = 2)

p_accept <- c(0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1)
ratio <- sapply(p_accept, function(p) {
  a <- if (p < 1) qchisq(p, k) else Inf
  v_a <- if (p < 1) pchisq(a, k + 2) / pchisq(a, k) else 1
  c(emp = var(tau_hat[m_stat <= a]) / var(tau_hat), theory = 1 - (1 - v_a) * r2)
})
plot(p_accept, ratio["emp", ], log = "x", pch = 16, ylim = c(0, 1),
     xlab = "acceptance probability", ylab = "variance ratio")
lines(p_accept, ratio["theory", ], col = "red")
par(op)
