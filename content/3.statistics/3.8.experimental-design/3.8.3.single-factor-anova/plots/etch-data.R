# Etch rate data of the plasma etching experiment: points, level means and box plots.
y <- c(575, 542, 530, 539, 570,
       565, 593, 590, 579, 610,
       600, 651, 610, 637, 629,
       725, 700, 715, 685, 710)
X <- rep(c(160, 180, 200, 220), each = 5)
etch.rate <- data.frame(RF = as.factor(X), rate = y)

op <- par(mfrow = c(1, 2))
stripchart(rate ~ RF, data = etch.rate, vertical = TRUE, method = "jitter", pch = 19,
           xlab = "RF power (W)", ylab = "etch rate (Angstrom/min)",
           main = "Observations and level means")
means <- tapply(etch.rate$rate, etch.rate$RF, mean)
points(1:4, means, pch = 18, cex = 2, col = "red")
abline(h = mean(etch.rate$rate), lty = 2, col = "gray")
boxplot(rate ~ RF, data = etch.rate, xlab = "RF power (W)", main = "Box plots by power level")
par(op)
