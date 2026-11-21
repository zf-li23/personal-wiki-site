# Rocket propellant Latin square: data, boxplots by factor, ANOVA of the Latin square and of an RCBD.
Rocket <- data.frame(
  Batch    = factor(rep(1:5, each = 5)),
  Operator = factor(rep(1:5, times = 5)),
  Treat    = factor(c("A", "B", "C", "D", "E",  "B", "C", "D", "E", "A",
                      "C", "D", "E", "A", "B",  "D", "E", "A", "B", "C",
                      "E", "A", "B", "C", "D")),
  Rate     = c(24, 20, 19, 24, 24,  17, 24, 30, 27, 36,  18, 38, 26, 27, 21,
               26, 31, 26, 23, 22,  22, 30, 20, 29, 31))
par(mfcol = c(1, 3))
plot(Rate ~ Operator + Batch + Treat, Rocket, las = 1)
par(mfcol = c(1, 1))
summary(aov(Rate ~ Treat + Batch + Operator, Rocket))   # Latin square
summary(aov(Rate ~ Treat + Operator, Rocket))           # batches ignored (RCBD)
TukeyHSD(aov(Rate ~ Treat + Batch + Operator, Rocket), "Treat")
