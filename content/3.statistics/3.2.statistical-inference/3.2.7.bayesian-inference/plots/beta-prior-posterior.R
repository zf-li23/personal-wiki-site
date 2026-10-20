# Beta prior densities, and a Beta(14, 6) prior updated by binomial data with n = 10 and n = 100.
theta <- seq(0.001, 0.999, length.out = 500)
op <- par(mfrow = c(1, 2))

priors <- rbind(c(1, 1), c(20, 20), c(1, 3), c(8, 2))
cols <- c("steelblue", "darkorange", "darkgreen", "firebrick")
matplot(theta, apply(priors, 1, function(p) dbeta(theta, p[1], p[2])), type = "l", lty = 1,
        lwd = 1.8, col = cols, ylim = c(0, 5.5), xlab = "theta", ylab = "density",
        main = "Beta priors")
legend("top", bty = "n", cex = 0.8, legend = sprintf("Beta(%g, %g)", priors[, 1], priors[, 2]),
       col = cols, lwd = 1.8)

# conjugate update: Beta(a0, b0) prior and x successes in n trials give Beta(a0 + x, b0 + n - x)
a0 <- 14; b0 <- 6   # prior mean 0.7, sd 0.1
data <- data.frame(n = c(10, 100), x = c(3, 30))
dens <- cbind(dbeta(theta, a0, b0),
              dbeta(theta, a0 + data$x[1], b0 + data$n[1] - data$x[1]),
              dbeta(theta, a0 + data$x[2], b0 + data$n[2] - data$x[2]))
matplot(theta, dens, type = "l", lty = 1, lwd = 1.8, col = cols[1:3],
        xlab = "theta", ylab = "", main = "Prior and posteriors")
abline(v = 0.3, lty = 2, col = "grey50")
legend("topright", bty = "n", cex = 0.8,
       legend = c("prior Beta(14, 6)", "posterior, n = 10, x = 3", "posterior, n = 100, x = 30"),
       col = cols[1:3], lwd = 1.8)
par(op)
