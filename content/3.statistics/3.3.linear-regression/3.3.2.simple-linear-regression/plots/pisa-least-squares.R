# Least squares fit to the Leaning Tower of Pisa data, with the residuals drawn as vertical segments.
year <- 75:87
lean <- c(642, 644, 656, 667, 673, 688, 696, 698, 713, 717, 725, 742, 757)

fit <- lm(lean ~ year)
b <- coef(fit)
sse <- sum(residuals(fit)^2)

plot(year, lean, pch = 19, col = "steelblue",
     xlab = "year (19xx)", ylab = "lean (0.1 mm above 2.9 m)",
     main = sprintf("Leaning Tower of Pisa: SSE = %.1f, MSE = %.2f", sse, sse / df.residual(fit)))
segments(year, fitted(fit), year, lean, col = "darkorange", lwd = 1.5)
abline(fit, col = "firebrick", lwd = 2)
legend("topleft", bty = "n", cex = 0.8,
       legend = c("observed lean", "residuals", sprintf("Y_hat = %.2f + %.4f X", b[1], b[2])),
       col = c("steelblue", "darkorange", "firebrick"), pch = c(19, NA, NA), lty = c(NA, 1, 1))
