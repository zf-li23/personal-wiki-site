# Exact density of (S_n - n)/sqrt(n) for i.i.d. Exp(1) summands (S_n ~ Gamma(n, 1)) versus the N(0,1) density.
z <- seq(-4, 4, length.out = 800)
ns <- c(1, 2, 5, 30)
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")

plot(z, dnorm(z), type = "l", lwd = 2, lty = 2, ylim = c(0, 0.75), xlab = "z", ylab = "density",
     main = "Standardized sums of Exp(1): skewness fades like 1/sqrt(n)")
for (j in seq_along(ns)) {
  n <- ns[j]
  lines(z, dgamma(n + sqrt(n) * z, shape = n, rate = 1) * sqrt(n), col = cols[j], lwd = 1.5)
}
legend("topright", bty = "n", lty = c(rep(1, 4), 2), lwd = c(rep(1.5, 4), 2),
       col = c(cols, "black"), legend = c(paste("n =", ns), "N(0, 1)"))
