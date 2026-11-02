# Etch rate against RF power: level means, linear and quadratic fits.
Etch <- data.frame(Power = factor(rep(c(160, 180, 200, 220), each = 5)),
                   Rate = c(575, 542, 530, 539, 570, 565, 593, 590, 579, 610,
                            600, 651, 610, 637, 629, 725, 700, 715, 685, 710))
x <- as.numeric(as.character(Etch$Power))
lin <- lm(Rate ~ x, data = Etch)
quad <- lm(Rate ~ x + I(x^2), data = Etch)
fem <- lm(Rate ~ Power, data = Etch)
anova(lin, fem)                                   # lack-of-fit test of the straight line
plot(x, Etch$Rate, xlab = "RF power x (W)", ylab = "etch rate",
     main = "Quantitative factor: regression vs fixed effects")
points(c(160, 180, 200, 220), tapply(Etch$Rate, Etch$Power, mean), pch = 15, col = "red", cex = 1.5)
abline(lin, col = "darkorange")
xx <- seq(155, 225, length.out = 200)
lines(xx, predict(quad, data.frame(x = xx)), lty = 2, col = "darkgreen")
