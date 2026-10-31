# Jarzynski equality and Crooks theorem for a dragged harmonic trap on a double-well landscape (base R).
set.seed(0)
k <- 5; l0 <- -1.5; l1 <- 2.0; tau <- 2; dt <- 1e-3; n <- 3000
U  <- function(x) 3 * (x^2 - 1)^2
dU <- function(x) 12 * x * (x^2 - 1)
xg <- seq(-4, 5, length.out = 20001)
lnZ <- function(lam) { H <- U(xg) + 0.5 * k * (xg - lam)^2; m <- min(H)
  -m + log(sum(exp(-(H - m))) * (xg[2] - xg[1])) }
dF <- -(lnZ(l1) - lnZ(l0))

equilibrium <- function(lam, size) {
  w <- exp(-(U(xg) + 0.5 * k * (xg - lam)^2)); cw <- cumsum(w)
  approx(cw, xg, xout = runif(size) * cw[length(cw)], ties = "ordered")$y
}
pull <- function(la, lb) {
  steps <- round(tau / dt); dl <- (lb - la) / steps
  x <- equilibrium(la, n); lam <- la; W <- numeric(n)
  for (s in 1:steps) {
    W <- W - k * (x - lam) * dl
    lam <- lam + dl
    x <- x + (-dU(x) - k * (x - lam)) * dt + sqrt(2 * dt) * rnorm(n)
  }
  W
}
WF <- pull(l0, l1); WR <- pull(l1, l0)
jarzynski <- function(w) -(log(mean(exp(-(w - min(w))))) - min(w))
cat(sprintf("exact dF = %.3f, Jarzynski (forward) = %.3f, <W> = %.3f\n", dF, jarzynski(WF), mean(WF)))

par(mfrow = c(1, 2))
br <- seq(min(c(WF, -WR)) - 0.5, max(c(WF, -WR)) + 0.5, length.out = 50)
hist(WF, breaks = br, freq = FALSE, col = rgb(0.2, 0.4, 0.8, 0.5), main = "Work distributions", xlab = "W / kT")
hist(-WR, breaks = br, freq = FALSE, col = rgb(0.9, 0.4, 0.2, 0.5), add = TRUE)
abline(v = dF, lty = 2)
Ns <- unique(round(10^seq(0, log10(n), length.out = 25)))
est <- sapply(Ns, function(N) median(replicate(200, jarzynski(sample(WF, N)))))
plot(Ns, est, log = "x", type = "l", xlab = "N", ylab = "estimate / kT", main = "Jarzynski estimate")
abline(h = dF, lty = 2); abline(h = mean(WF), lty = 3)
