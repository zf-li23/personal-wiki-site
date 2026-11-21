# Tukey intervals for the graft pressures with and without the block term.
graft <- data.frame(
  PSI   = factor(rep(c(8500, 8700, 8900, 9100), each = 6)),
  Block = factor(rep(1:6, times = 4)),
  Yield = c(90.3, 89.2, 98.2, 93.9, 87.4, 97.9,
            92.5, 89.5, 90.6, 94.7, 87.0, 95.8,
            85.5, 90.8, 89.6, 86.2, 88.0, 93.4,
            82.5, 89.5, 85.6, 87.4, 78.9, 90.7))
rcbd <- TukeyHSD(aov(Yield ~ PSI + Block, data = graft), "PSI")
crd  <- TukeyHSD(aov(Yield ~ PSI, data = graft), "PSI")
par(mfrow = c(1, 2))
plot(rcbd, las = 1, cex.axis = 0.75); title(sub = "RCBD")
plot(crd,  las = 1, cex.axis = 0.75); title(sub = "blocks ignored")
par(mfrow = c(1, 1))
