# Importance sampling: running estimates with a good and a bad proposal, and the
# estimation of the rare event probability P(X > 4) for X ~ N(0, 1).
set.seed(0)
alpha <- 0.5; beta <- 2.5; n <- 5000
run_est <- function(a, b) {
  y <- rgamma(n, shape = a, rate = b)
  w <- dgamma(y, alpha, beta) / dgamma(y, a, b)   # importance weights p / q
  cumsum(w) / seq_len(n)                          # running estimate of E_p[1] = 1
}
par(mfrow = c(1, 2))
plot(run_est(2, 2), type = "l", log = "x", col = "firebrick", ylim = c(0, 2),
     xlab = "number of proposals m", ylab = "running IS estimate of E_p[1]")
lines(run_est(0.5, 1), col = "steelblue")
abline(h = 1, lty = 2)

x0 <- 4; m <- 1000
crude <- replicate(100, mean(rnorm(m) > x0))
is <- replicate(100, {
  y <- rnorm(m, mean = x0)
  w <- dnorm(y) / dnorm(y, mean = x0)
  mean(w * (y > x0))
})
stripchart(list(crude = crude, IS = is), vertical = TRUE, method = "jitter", pch = 20,
           col = c("firebrick", "steelblue"), ylab = "estimate of P(X > 4)")
abline(h = pnorm(x0, lower.tail = FALSE), lty = 2)
c(sd(crude), sd(is))
