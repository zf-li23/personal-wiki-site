# Calibrating an optical trap from the Brownian motion of the trapped bead (simulation; base R).
set.seed(0)
kT <- 4.11                          # pN nm
gamma <- 6 * pi * 0.89e-9 * 500     # pN s / nm
kappa <- 0.05                       # pN / nm
fs <- 1e5; Tt <- 2; n <- fs * Tt; dt <- 1 / fs
a <- exp(-dt * kappa / gamma)
sdv <- sqrt(kT / kappa * (1 - a^2))
x <- as.numeric(stats::filter(rnorm(n, 0, sdv), a, method = "recursive"))

# equipartition
kappa_eq <- kT / var(x)

# averaged one-sided power spectrum
seg <- 50; L <- n %/% seg
S <- 0
for (k in 1:seg) {
  w <- x[((k - 1) * L + 1):(k * L)]
  S <- S + (2 * dt / L) * Mod(fft(w))^2
}
S <- S / seg
f <- (0:(L - 1)) / (L * dt)
keep <- f > 5 & f < fs / 4
fit <- nls(S ~ D / (pi^2 * (fc^2 + f^2)), data = data.frame(S = S[keep], f = f[keep]),
           start = list(fc = 500, D = kT / gamma), weights = 1 / S[keep]^2)
fc <- coef(fit)["fc"]; D <- coef(fit)["D"]
kappa_psd <- 2 * pi * (kT / D) * fc

par(mfrow = c(1, 3))
plot((1:2000) * dt * 1e3, x[1:2000], type = "l", xlab = "time / ms", ylab = "x / nm")
hist(x, breaks = 60, freq = FALSE, main = sprintf("kappa = %.4f pN/nm", kappa_eq), xlab = "x / nm")
curve(dnorm(x, 0, sqrt(kT / kappa)), add = TRUE, col = "red")
plot(f[keep], S[keep], log = "xy", type = "l", xlab = "f / Hz", ylab = "PSD / (nm^2/Hz)",
     main = sprintf("fc = %.0f Hz, kappa = %.4f pN/nm", fc, kappa_psd))
lines(f[keep], predict(fit), col = "red", lwd = 2)
