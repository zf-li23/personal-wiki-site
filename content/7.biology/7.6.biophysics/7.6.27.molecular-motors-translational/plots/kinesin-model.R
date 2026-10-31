# Three-state kinesin model (Formula 27.3.4): force-velocity curves and the Michaelis-Menten parameters (base R).
kT <- 4.1; a <- 8.2                                   # pN nm, nm
kon <- 1.5; koff <- 10; k10 <- 200; k2 <- 200          # 1/(uM s), 1/s
kb0 <- k10 / 800; d0 <- 0.8; d1 <- 1.2; db <- 2.6      # 1/s, nm
velocity <- function(F, atp) {
  u0 <- kon * atp * exp(-d0 * F / kT)
  k1 <- k10 * exp(-d1 * F / kT)
  kb <- kb0 * exp(db * F / kT)
  p1 <- 1 / ((koff + k1 + kb) / u0 + 1 + (k1 + kb) / k2)
  a * p1 * (k1 - kb)
}
F <- seq(0, 8, length.out = 400)
plot(F, velocity(F, 2000), type = "l", lwd = 2, ylim = c(-150, 900),
     xlab = "load F / pN", ylab = "V / (nm/s)")
lines(F, 10 * velocity(F, 5), lwd = 2, col = 4)
abline(h = 0, lty = 3)
Fs <- kT * log(k10 / kb0) / (d1 + db)
abline(v = Fs, lty = 2)
legend("topright", c("2 mM ATP", "5 uM ATP (x10)"), col = c(1, 4), lwd = 2, bty = "n")
# Michaelis-Menten fit at each load recovers Vmax(F) and KM(F)
atp <- 10^seq(0, 4, length.out = 40)
for (Fl in c(1.05, 3.59, 5.63)) {
  v <- velocity(Fl, atp)
  fit <- nls(v ~ Vm * atp / (Km + atp), start = list(Vm = max(v), Km = 50))
  cat(sprintf("F = %.2f pN: Vmax = %.0f nm/s, KM = %.0f uM\n", Fl, coef(fit)["Vm"], coef(fit)["Km"]))
}
cat(sprintf("stall force = %.2f pN\n", Fs))
