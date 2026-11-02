# Residual diagnostics for the plasma etching experiment.
etch <- data.frame(
  power = factor(rep(c(160, 180, 200, 220), each = 5)),
  rate = c(575, 542, 530, 539, 570, 565, 593, 590, 579, 610,
           600, 651, 610, 637, 629, 725, 700, 715, 685, 710),
  run = c(13, 14, 8, 5, 4, 18, 9, 6, 16, 17, 7, 19, 10, 20, 1, 2, 3, 15, 11, 12))
fit <- aov(rate ~ power, data = etch)
e <- residuals(fit)
d <- e / sqrt(sum(e^2) / df.residual(fit))   # standardized residuals

op <- par(mfrow = c(2, 2))
plot(fitted(fit), e, xlab = "fitted value (level mean)", ylab = "residual",
     main = "Residuals vs fitted"); abline(h = 0, col = "gray")
qqnorm(d, main = "Normal probability plot"); qqline(d)
o <- order(etch$run)
plot(etch$run[o], e[o], type = "b", xlab = "run order", ylab = "residual",
     main = "Residuals vs run order"); abline(h = 0, col = "gray")
plot(as.numeric(as.character(etch$power)), d, ylim = c(-3.6, 3.6),
     xlab = "RF power (W)", ylab = "standardized residual",
     main = "Standardized residuals by level")
abline(h = c(-3, 3), lty = 2, col = "red"); abline(h = 0, col = "gray")
par(op)
