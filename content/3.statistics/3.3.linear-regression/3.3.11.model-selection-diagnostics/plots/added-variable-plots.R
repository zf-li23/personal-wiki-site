# Added-variable plots: the curvature of a quadratic effect shows up after adjusting for the other variable.
set.seed(0)
n <- 40
income <- runif(n, 25, 80)
risk <- pmin(pmax(5 + 0.03 * (income - 50) + rnorm(n, 0, 2), 1), 10)
insur <- -100 + 0.08 * income^2 + 5 * risk + rnorm(n, 0, 8)

fit <- lm(insur ~ income + risk)
# car::avPlots(fit) draws the same plots; here they are built from residuals by hand
op <- par(mfrow = c(1, 2), oma = c(0, 0, 2, 0))
for (name in c("income", "risk")) {
  other <- setdiff(c("income", "risk"), name)
  ry <- residuals(lm(reformulate(other, "insur")))
  rx <- residuals(lm(reformulate(other, name)))
  slope <- coef(lm(ry ~ rx - 1))   # equals the coefficient of name in fit
  plot(rx, ry, pch = 19, col = "steelblue", xlab = paste(name, "| others"), ylab = "insurance | others")
  abline(0, slope, col = "firebrick", lwd = 2)
  leg <- sprintf("slope = b_k = %.2f", slope)
  if (name == "income") {
    quad <- lm(ry ~ rx + I(rx^2))
    o <- order(rx)
    lines(rx[o], fitted(quad)[o], col = "forestgreen", lwd = 1.5, lty = 2)
    leg <- c(leg, "quadratic fit to the plot")
  }
  legend("topleft", bty = "n", cex = 0.8, lwd = c(2, 1.5)[seq_along(leg)], lty = c(1, 2)[seq_along(leg)],
         col = c("firebrick", "forestgreen")[seq_along(leg)], legend = leg)
}
mtext("Added-variable plots for a model that is linear in income and risk", outer = TRUE)
par(op)
