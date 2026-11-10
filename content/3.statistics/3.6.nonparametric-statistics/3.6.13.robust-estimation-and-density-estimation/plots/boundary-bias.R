# Boundary bias at a hard boundary: kernel and local linear density estimates for Exp(1) data.
library(KernSmooth)
set.seed(0)
x <- rexp(500)
h <- 0.3
plot(density(x, bw = h), xlim = c(-1, 4), ylim = c(0, 1.15), col = "steelblue", lwd = 2,
     main = "Boundary bias at x = 0", xlab = "x")
curve(dexp(x), from = 0, to = 4, add = TRUE, lty = 2)
ll <- locpoly(x, bandwidth = h, degree = 1, range.x = c(0, max(x)), gridsize = 401)
lines(ll$x, ll$y, col = "firebrick", lwd = 2)
abline(v = 0, col = "grey50")
rug(x)
legend("topright", c("true density", "kernel", "local linear"), lty = c(2, 1, 1),
       col = c("black", "steelblue", "firebrick"), lwd = c(1, 2, 2), bty = "n")
