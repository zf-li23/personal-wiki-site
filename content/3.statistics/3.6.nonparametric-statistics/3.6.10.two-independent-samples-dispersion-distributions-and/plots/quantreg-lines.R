# Quantile regression lines and the slope as a function of tau, for simulated heteroscedastic expenditure data.
library(quantreg)
set.seed(0)
n <- 235
income <- exp(rnorm(n, log(900), 0.45))
food <- 80 + 0.5 * income + 0.12 * income * (rgamma(n, 3, 1) - 3) / sqrt(3)
taus <- seq(0.05, 0.95, by = 0.05)
fits <- rq(food ~ income, tau = taus)
ols <- lm(food ~ income)

op <- par(mfrow = c(1, 2))
plot(income, food, pch = 19, cex = 0.5, col = "gray50",
     xlab = "household income", ylab = "food expenditure", main = "Quantile regression lines")
for (t in c(0.1, 0.25, 0.5, 0.75, 0.9)) abline(rq(food ~ income, tau = t), col = "steelblue")
abline(ols, col = "firebrick", lty = 2, lwd = 2)
plot(summary(fits, se = "boot", R = 200), parm = "income", main = "Slope on income")
par(op)
# The same model fitted to the real Engel data: rq(foodexp ~ income, tau = 0.5, data = engel)
