# Vascular graft experiment (RCBD): profiles of the batches and pressure means.
graft <- data.frame(
  PSI   = factor(rep(c(8500, 8700, 8900, 9100), each = 6)),
  Block = factor(rep(1:6, times = 4)),
  Yield = c(90.3, 89.2, 98.2, 93.9, 87.4, 97.9,
            92.5, 89.5, 90.6, 94.7, 87.0, 95.8,
            85.5, 90.8, 89.6, 86.2, 88.0, 93.4,
            82.5, 89.5, 85.6, 87.4, 78.9, 90.7))
par(mfrow = c(1, 2))
with(graft, interaction.plot(PSI, Block, Yield, xlab = "extrusion pressure (psi)",
                             ylab = "yield (%)", trace.label = "batch", bty = "L"))
with(graft, stripchart(Yield ~ Block, vertical = TRUE, pch = as.integer(PSI),
                       xlab = "batch of resin (block)", ylab = "yield (%)"))
points(1:6, tapply(graft$Yield, graft$Block, mean), pch = "-", cex = 3)
abline(h = mean(graft$Yield), lty = 2, col = "gray")
par(mfrow = c(1, 1))
