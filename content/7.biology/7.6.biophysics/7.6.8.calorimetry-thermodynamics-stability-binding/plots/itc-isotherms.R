# Isothermal titration calorimetry of 1:1 binding: simulated isotherms for several Wiseman c values
# and a nonlinear least-squares fit of n, Ka and dH (overflow-cell model, displaced-volume correction).
set.seed(0)
V0 <- 200e-6                       # cell volume, L
dv <- c(0.4e-6, rep(2.0e-6, 19))   # injection volumes, L
M0 <- 20e-6                        # macromolecule in the cell, M
L0 <- 220e-6                       # ligand in the syringe, M

concentrations <- function(M0, L0) {
  v <- cumsum(dv)
  list(Mt = M0 * (1 - v / (2 * V0)) / (1 + v / (2 * V0)),
       Lt = L0 * (v / V0) * (1 - v / (2 * V0)))
}

bound <- function(Mt, Lt, n, Ka) {
  s <- n * Mt + Lt + 1 / Ka
  (s - sqrt(s^2 - 4 * n * Mt * Lt)) / 2
}

# heat of each injection in microjoules (dH in kJ/mol)
heats <- function(n, Ka, dH) {
  cc <- concentrations(M0, L0)
  Q <- V0 * dH * 1e3 * bound(cc$Mt, cc$Lt, n, Ka) * 1e6
  Qprev <- c(0, Q[-length(Q)])
  Q - Qprev + dv / V0 * (Q + Qprev) / 2
}

cc <- concentrations(M0, L0)
ratio <- cc$Lt / cc$Mt
norm <- 1 / (dv * L0 * 1e6) / 1e3   # converts uJ per injection to kJ per mol of injectant
n_true <- 1; dH_true <- -45

par(mfrow = c(1, 2))
cols <- c("grey50", "steelblue", "purple", "firebrick", "darkcyan")
cs <- c(0.5, 5, 50, 500, 5000)
plot(NA, xlim = c(0, 2.4), ylim = c(-47, 1), xlab = "molar ratio [L]t/[M]t",
     ylab = "heat per mol injectant (kJ/mol)", main = "Wiseman c sets the shape")
for (k in seq_along(cs)) {
  Ka <- cs[k] / (n_true * M0)
  q <- heats(n_true, Ka, dH_true) * norm
  lines(ratio[-1], q[-1], type = "b", pch = 19, cex = 0.6, col = cols[k])
}
abline(v = 1, lty = 3)
legend("bottomright", legend = paste("c =", cs), col = cols, pch = 19, bty = "n")

# fit the c = 50 experiment with Gaussian noise of 0.15 uJ (the first injection is discarded)
Ka50 <- 50 / (n_true * M0)
y <- heats(n_true, Ka50, dH_true) + rnorm(length(dv), 0, 0.15)
d <- data.frame(i = seq_along(dv), y = y)[-1, ]
fit <- nls(y ~ heats(n, 10^logK, dH)[i], data = d,
           start = list(n = 0.9, logK = log10(Ka50) - 0.5, dH = -35))
print(summary(fit))
est <- coef(fit)
cat(sprintf("Kd = %.0f nM (true %.0f nM)\n", 1e9 / 10^est["logK"], 1e9 / Ka50))

plot(ratio[-1], d$y * norm[-1], pch = 19, col = "purple", xlab = "molar ratio [L]t/[M]t",
     ylab = "heat per mol injectant (kJ/mol)", main = "Fit at c = 50")
lines(ratio[-1], heats(est["n"], 10^est["logK"], est["dH"])[-1] * norm[-1], col = "purple")
