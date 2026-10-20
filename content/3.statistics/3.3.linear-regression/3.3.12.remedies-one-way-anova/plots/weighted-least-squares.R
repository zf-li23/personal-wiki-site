# WLS versus OLS for simulated data whose error standard deviation grows linearly with X.
set.seed(0)
n <- 54
x <- sort(runif(n, 20, 60))
sdev <- 0.25 * x - 2.0
y <- 56 + 0.58 * x + rnorm(n, 0, sdev)

ols <- lm(y ~ x)
e <- residuals(ols)
# stage 2: regress |e| on x to estimate the standard deviation of each case
sfit <- lm(abs(e) ~ x)
w <- 1 / fitted(sfit)^2
wls <- lm(y ~ x, weights = w)
print(summary(wls))

op <- par(mfrow = c(1, 2))
plot(x, y, pch = 19, col = "steelblue", xlab = "X (age)", ylab = "Y", main = "OLS and WLS fits")
abline(ols, col = "darkorange", lwd = 1.6)
abline(wls, col = "firebrick", lwd = 1.6, lty = 2)
legend("topleft", bty = "n", cex = 0.8, pch = c(19, NA, NA), lty = c(NA, 1, 2),
       col = c("steelblue", "darkorange", "firebrick"),
       legend = c("data", sprintf("OLS: slope %.3f", coef(ols)[2]), sprintf("WLS: slope %.3f", coef(wls)[2])))

plot(x, abs(e), pch = 19, col = "steelblue", xlab = "X (age)", ylab = "absolute residual",
     main = "Estimating the standard deviation")
abline(sfit, col = "firebrick", lwd = 1.6)
legend("topleft", bty = "n", cex = 0.8, pch = c(19, NA), lty = c(NA, 1), col = c("steelblue", "firebrick"),
       legend = c("|OLS residual|", "fitted sigma_hat(X)"))
par(op)
