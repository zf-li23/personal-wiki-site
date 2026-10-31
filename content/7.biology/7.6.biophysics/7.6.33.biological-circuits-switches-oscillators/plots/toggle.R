# Toggle switch du/dt = -u + a/(1 + v^n), dv/dt = -v + a/(1 + u^n): nullclines, trajectories and
# the fixed points against a (n = 2), using deSolve for the integration.
library(deSolve)
n <- 2
toggle <- function(t, y, a) list(c(-y[1] + a / (1 + y[2]^n), -y[2] + a / (1 + y[1]^n)))
for (a in c(1, 3)) {
  s <- seq(0, 3.4, length.out = 300)
  plot(a / (1 + s^n), s, type = "l", col = "blue", xlim = c(0, 3.4), ylim = c(0, 3.4),
       xlab = "u", ylab = "v", main = paste("alpha =", a))
  lines(s, a / (1 + s^n), col = "red")
  for (y0 in list(c(0.2, 3.2), c(3.2, 0.3), c(0.1, 0.4), c(1.5, 1.6))) {
    out <- ode(y0, seq(0, 15, 0.05), toggle, a)
    lines(out[, 2], out[, 3], col = "purple")
  }
}
# fixed points: roots of u = a / (1 + (a / (1 + u^n))^n) on (0, a)
fp <- function(a) {
  u <- seq(1e-6, a, length.out = 20001)
  g <- -u + a / (1 + (a / (1 + u^n))^n)
  u[which(diff(sign(g)) != 0)]
}
as <- seq(0.3, 5, 0.02)
plot(NULL, xlim = range(as), ylim = c(0, 5), xlab = "alpha", ylab = "u*")
for (a in as) points(rep(a, length(fp(a))), fp(a), pch = 16, cex = 0.3)
abline(v = 2, lty = 3)   # pitchfork at alpha = 2 for n = 2
