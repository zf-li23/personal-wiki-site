# Residual diagnostics for the vascular graft RCBD (additive model).
graft <- data.frame(
  PSI   = factor(rep(c(8500, 8700, 8900, 9100), each = 6)),
  Block = factor(rep(1:6, times = 4)),
  Yield = c(90.3, 89.2, 98.2, 93.9, 87.4, 97.9,
            92.5, 89.5, 90.6, 94.7, 87.0, 95.8,
            85.5, 90.8, 89.6, 86.2, 88.0, 93.4,
            82.5, 89.5, 85.6, 87.4, 78.9, 90.7))
graft.aov <- aov(Yield ~ PSI + Block, data = graft)
par(mfcol = c(2, 2))
plot(graft.aov, which = 1:2)
stripchart(residuals(graft.aov) ~ graft$PSI, vertical = TRUE, pch = 1,
           xlab = "extrusion pressure (psi)", ylab = "residual")
abline(h = 0, col = "gray")
stripchart(residuals(graft.aov) ~ graft$Block, vertical = TRUE, pch = 1,
           xlab = "batch of resin (block)", ylab = "residual")
abline(h = 0, col = "gray")
par(mfcol = c(1, 1))
