# Null distribution of D_n (n = 30) for normal samples with known versus estimated mu and sigma.
set.seed(0)
n <- 30; reps <- 20000
d_known <- replicate(reps, ks.test(rnorm(n), "pnorm")$statistic)
d_est <- replicate(reps, { x <- rnorm(n); ks.test(as.vector(scale(x)), "pnorm")$statistic })
hist(d_known, breaks = 60, freq = FALSE, col = adjustcolor("steelblue", 0.4), border = NA,
     xlim = c(0, 0.35), main = "", xlab = "D_n (n = 30)")
hist(d_est, breaks = 60, freq = FALSE, col = adjustcolor("darkorange", 0.4), border = NA, add = TRUE)
abline(v = quantile(d_known, 0.95), col = "steelblue", lty = 2)
abline(v = quantile(d_est, 0.95), col = "darkorange", lty = 2)
abline(v = 0.192, col = "firebrick")
# the Lilliefors test itself: nortest::lillie.test(x)
