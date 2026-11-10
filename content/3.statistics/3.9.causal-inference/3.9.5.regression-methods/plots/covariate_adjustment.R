# Sampling distributions of three estimators of the average effect in a simulated CRE.
set.seed(0)
n <- 100; reps <- 3000

one_draw <- function(p, slope_c, slope_t) {
  x <- rnorm(n)
  y0 <- slope_c * x + rnorm(n)
  y1 <- 1 + slope_t * x + rnorm(n)                 # tau_sp = 1
  w <- seq_len(n) %in% sample(n, round(p * n))
  y <- ifelse(w, y1, y0)
  xc <- x - mean(x)
  c(dif = mean(y[w]) - mean(y[!w]),
    ols = unname(coef(lm(y ~ w + x))["wTRUE"]),
    inter = unname(coef(lm(y ~ w + x + w:xc))["wTRUE"]))
}

par(mfrow = c(1, 2))
est <- t(replicate(reps, one_draw(0.5, 1, 1)))
cols <- c("steelblue", "darkorange", "forestgreen")
plot(density(est[, "dif"]), col = cols[1], lwd = 2, xlim = c(-0.2, 2.2),
     ylim = c(0, 2.3), main = "Common slope, p = 0.5", xlab = "estimate")
lines(density(est[, "ols"]), col = cols[2], lwd = 2)
lines(density(est[, "inter"]), col = cols[3], lwd = 2)
abline(v = 1, lty = 3)
print(apply(est, 2, sd))

ps <- seq(0.1, 0.9, by = 0.1)
sds <- t(sapply(ps, function(p) apply(t(replicate(1500, one_draw(p, -1, 3))), 2, sd)))
matplot(ps, sds, type = "b", pch = 19, lty = 1, col = cols,
        xlab = "proportion treated p", ylab = "sampling sd",
        main = "Slopes -1 (control) and 3 (treated)")
legend("top", c("difference in means", "OLS with covariate", "OLS with interaction"),
       col = cols, lty = 1, bty = "n")
