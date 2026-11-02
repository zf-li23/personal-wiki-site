# Soft drink bottling: main effect and interaction plots, three-way ANOVA.
Bottle <- expand.grid(rep = 1:2, speed = c(200, 250), pressure = c(25, 30),
                      carbonation = c(10, 12, 14))
Bottle$deviation <- c(-3, -1, -1, 0, -1, 0, 1, 1,
                      0, 1, 2, 1, 2, 3, 6, 5,
                      5, 4, 7, 6, 7, 9, 10, 11)
Bottle[c("speed", "pressure", "carbonation")] <-
  lapply(Bottle[c("speed", "pressure", "carbonation")], factor)
par(mfrow = c(2, 3))
with(Bottle, plot(carbonation, deviation, main = "Percent carbonation (A)"))
with(Bottle, lines(tapply(deviation, carbonation, mean), col = 2, type = "b"))
with(Bottle, plot(pressure, deviation, main = "Pressure (B)"))
with(Bottle, lines(tapply(deviation, pressure, mean), col = 2, type = "b"))
with(Bottle, plot(speed, deviation, main = "Line speed (C)"))
with(Bottle, lines(tapply(deviation, speed, mean), col = 2, type = "b"))
with(Bottle, interaction.plot(carbonation, pressure, deviation, bty = "L",
                              main = "Interaction of A and B"))
with(Bottle, interaction.plot(pressure, speed, deviation, bty = "L",
                              main = "Interaction of B and C"))
with(Bottle, interaction.plot(carbonation, speed, deviation, bty = "L",
                              main = "Interaction of A and C"))
par(mfrow = c(1, 1))
summary(aov(deviation ~ carbonation * pressure * speed, data = Bottle))
