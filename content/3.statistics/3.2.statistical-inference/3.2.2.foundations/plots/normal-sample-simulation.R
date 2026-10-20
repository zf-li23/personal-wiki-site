# Simulation: 1000 samples of size 100 from N(1, 4); distributions of the sample mean, S^2 and the t statistic.
set.seed(0)
n <- 100
reps <- 1000
a <- 1
sigma <- 2
y <- matrix(rnorm(reps * n, a, sigma), reps, n)
xbar <- rowMeans(y)
s2 <- apply(y, 1, var)
tstat <- sqrt(n) * (xbar - a) / sqrt(s2)

# histogram of the simulated values with the theoretical density on top
show <- function(values, dens, main, label) {
  g <- seq(min(values), max(values), length.out = 300)
  h <- hist(values, breaks = 30, plot = FALSE)
  plot(h, freq = FALSE, col = adjustcolor("steelblue", 0.6), border = "white",
       ylim = c(0, max(h$density, dens(g))), main = main, xlab = "")
  lines(g, dens(g), col = "firebrick", lwd = 1.5)
  legend("topright", bty = "n", cex = 0.8, legend = label, col = "firebrick", lwd = 1.5)
}

op <- par(mfrow = c(1, 3), oma = c(0, 0, 2, 0))
show(xbar, function(g) dnorm(g, a, sigma / sqrt(n)), "sample mean", "N(a, sigma^2/n)")
abline(v = a, col = "darkgreen", lwd = 1.2)
show(s2, function(g) dchisq((n - 1) * g / sigma^2, n - 1) * (n - 1) / sigma^2,
     "sample variance S^2", "sigma^2 chi2(n-1)/(n-1)")
abline(v = sigma^2, col = "darkgreen", lwd = 1.2)
show(tstat, function(g) dt(g, n - 1), "sqrt(n)(mean - a)/S", "t(n-1)")
mtext("1000 samples of size n = 100 from N(1, 4)", outer = TRUE, cex = 1.1)
par(op)
