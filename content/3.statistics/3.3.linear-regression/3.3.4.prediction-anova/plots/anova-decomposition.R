# Partition of the total deviation Y_i - Y_bar into Y_i - Y_hat_i and Y_hat_i - Y_bar (Toluca data).
x <- c(80, 30, 50, 90, 70, 60, 120, 80, 100, 50, 40, 70, 90, 20, 110, 100, 30, 50, 90, 110, 30, 90, 40, 80, 70)
y <- c(399, 121, 221, 376, 361, 224, 546, 352, 353, 157, 160, 252, 389, 113, 435, 420, 212, 268, 377, 421, 273,
       468, 244, 342, 323)

fit <- lm(y ~ x)
tab <- anova(fit)
print(tab)
ssr <- tab[["Sum Sq"]][1]
sse <- tab[["Sum Sq"]][2]
ssto <- ssr + sse
ybar <- mean(y)
yhat <- fitted(fit)
pick <- c(1, 2)   # the lots (80, 399) and (30, 121)

titles <- c(sprintf("(a) Y_i - Y_bar: SSTO = %.0f", ssto),
            sprintf("(b) Y_i - Y_hat_i: SSE = %.0f", sse),
            sprintf("(c) Y_hat_i - Y_bar: SSR = %.0f", ssr))
op <- par(mfrow = c(1, 3))
for (k in 1:3) {
  plot(x, y, pch = 19, col = adjustcolor("steelblue", 0.35), xlab = "lot size",
       ylab = if (k == 1) "work hours" else "", main = titles[k])
  abline(h = ybar, lty = 2, col = "gray40")
  if (k > 1) abline(fit, lwd = 1.5)
  points(x[pick], y[pick], pch = 19, col = "steelblue", cex = 1.4)
  if (k == 1) {
    segments(x[pick], ybar, x[pick], y[pick], col = "firebrick", lwd = 2.5)
  } else if (k == 2) {
    segments(x[pick], yhat[pick], x[pick], y[pick], col = "darkorange", lwd = 2.5)
    points(x[pick], yhat[pick], pch = 15)
  } else {
    segments(x[pick], ybar, x[pick], yhat[pick], col = "forestgreen", lwd = 2.5)
    points(x[pick], yhat[pick], pch = 15)
  }
}
par(op)
