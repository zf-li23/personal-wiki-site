# Toluca data: pointwise confidence intervals, Working-Hotelling band and prediction intervals.
x <- c(80, 30, 50, 90, 70, 60, 120, 80, 100, 50, 40, 70, 90, 20, 110, 100, 30, 50, 90, 110, 30, 90, 40, 80, 70)
y <- c(399, 121, 221, 376, 361, 224, 546, 352, 353, 157, 160, 252, 389, 113, 435, 420, 212, 268, 377, 421, 273,
       468, 244, 342, 323)
n <- length(x)
fit <- lm(y ~ x)
b <- coef(fit)

new <- data.frame(x = seq(15, 125, length.out = 300))
conf <- predict(fit, new, interval = "confidence", level = 0.95)
pred <- predict(fit, new, interval = "prediction", level = 0.95)
se_mean <- predict(fit, new, se.fit = TRUE)$se.fit
W <- sqrt(2 * qf(0.95, 2, n - 2))
wh_lo <- conf[, "fit"] - W * se_mean
wh_hi <- conf[, "fit"] + W * se_mean

g <- new$x
plot(x, y, type = "n", ylim = range(pred), xlab = "lot size", ylab = "work hours",
     main = "Toluca Company: intervals for the mean, the line and new observations", cex.main = 0.9)
polygon(c(g, rev(g)), c(pred[, "lwr"], rev(pred[, "upr"])), col = adjustcolor("forestgreen", 0.15), border = NA)
lines(g, wh_lo, col = "darkorange", lwd = 1.5, lty = 2)
lines(g, wh_hi, col = "darkorange", lwd = 1.5, lty = 2)
lines(g, conf[, "lwr"], col = "firebrick", lwd = 1.2)
lines(g, conf[, "upr"], col = "firebrick", lwd = 1.2)
lines(g, conf[, "fit"], lwd = 1.5)
points(x, y, pch = 19, col = "steelblue")
abline(v = mean(x), lty = 3, col = "gray")
legend("topleft", bty = "n", cex = 0.75, lwd = c(8, 1.5, 1.2, 1.5), lty = c(1, 2, 1, 1),
       col = c(adjustcolor("forestgreen", 0.15), "darkorange", "firebrick", "black"),
       legend = c("95% prediction intervals",
                  sprintf("95%% Working-Hotelling band (W = %.3f)", W),
                  sprintf("95%% pointwise confidence intervals (t = %.3f)", qt(0.975, n - 2)),
                  sprintf("Y_hat = %.2f + %.3f X", b[1], b[2])))
