# Lord's paradox: unchanged weight distributions but separated parallel regressions.
set.seed(0)
n <- 150
mu <- c(males = 70, females = 55)    # mean weight in kg, same in Sep and Jun
sd0 <- 7; rho <- 0.7                 # common sd and Sep-Jun correlation
sim <- lapply(names(mu), function(g) {
  x <- rnorm(n, mu[g], sd0)
  y <- mu[g] + rho * (x - mu[g]) + rnorm(n, 0, sd0 * sqrt(1 - rho^2))
  data.frame(sex = g, sep = x, jun = y)
})
d <- do.call(rbind, sim)
d$sex <- factor(d$sex, levels = names(mu))

fit <- lm(jun ~ sep + sex, data = d)   # parallel regression adjustment
print(coef(fit))

plot(d$sep, d$jun, col = c("steelblue", "firebrick")[d$sex], pch = c(19, 15)[d$sex],
     cex = 0.6, xlim = c(35, 95), ylim = c(35, 95), asp = 1,
     xlab = "weight in September / kg", ylab = "weight in June / kg",
     main = sprintf("common slope = %.2f, gap between lines = %.1f kg",
                    coef(fit)["sep"], -coef(fit)["sexfemales"]))
abline(0, 1, lty = 2, col = "gray")
abline(coef(fit)[1], coef(fit)[2], col = "steelblue", lwd = 2)
abline(coef(fit)[1] + coef(fit)[3], coef(fit)[2], col = "firebrick", lwd = 2)
points(mu, mu, pch = 4, cex = 2, lwd = 2)
legend("topleft", levels(d$sex), col = c("steelblue", "firebrick"), pch = c(19, 15), bty = "n")
