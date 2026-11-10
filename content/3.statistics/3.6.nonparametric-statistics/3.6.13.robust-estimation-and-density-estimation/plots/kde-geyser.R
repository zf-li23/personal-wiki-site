# Density estimates for the Old Faithful waiting times: kernel estimates with three bandwidths,
# then the kernel, local linear (KernSmooth::locpoly) and k-nearest-neighbor estimators.
library(KernSmooth)
x <- faithful$waiting
n <- length(x)
h0 <- bw.nrd0(x)                        # 0.9 min(s, IQR/1.34) n^(-1/5) = 3.99
op <- par(mfrow = c(1, 2), mar = c(4, 4, 2, 1))
hist(x, breaks = seq(40, 100, by = 4), freq = FALSE, col = "grey85", ylim = c(0, 0.07),
     xlim = c(30, 110), main = "Gaussian kernel, three bandwidths", xlab = "waiting time / min")
lines(density(x, bw = 1), col = "darkorange", lwd = 2)
lines(density(x, bw = h0), col = "steelblue", lwd = 2)
lines(density(x, bw = 10), col = "forestgreen", lwd = 2)
lines(density(x, bw = "SJ"), col = "black", lty = 2)
rug(x)

knn_density <- function(t, data, k) {
  sapply(t, function(t0) k / (2 * length(data) * sort(abs(data - t0))[k]))
}
grid <- seq(30, 110, length.out = 400)
plot(density(x, bw = h0), col = "steelblue", lwd = 2, xlim = c(30, 110), ylim = c(0, 0.07),
     main = "three estimators", xlab = "waiting time / min")
ll <- locpoly(x, bandwidth = h0, degree = 1)
lines(ll$x, ll$y, col = "firebrick", lwd = 2, lty = 2)
lines(grid, knn_density(grid, x, 50), col = "forestgreen", lwd = 2, lty = 3)
abline(h = 0, col = "grey40")
legend("topleft", c("kernel", "local linear", "k-NN, k = 50"), lty = 1:3,
       col = c("steelblue", "firebrick", "forestgreen"), lwd = 2, bty = "n")
par(op)
