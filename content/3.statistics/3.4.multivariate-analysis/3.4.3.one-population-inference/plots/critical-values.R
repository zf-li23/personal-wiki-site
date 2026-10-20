# Multipliers of individual, Bonferroni and T^2 intervals as functions of the dimension p (n = 200).
n <- 200
alpha <- 0.05
p <- 1:100
c_t <- rep(qt(1 - alpha / 2, n - 1), length(p))
c_bonf <- qt(1 - alpha / (2 * p), n - 1)
c_T2 <- sqrt(p * (n - 1) / (n - p) * qf(1 - alpha, p, n - p))

plot(p, c_T2, type = "l", lwd = 2, col = "darkorange", ylim = c(0, max(c_T2)),
     xlab = "dimension p", ylab = "multiplier c", main = "n = 200, alpha = 0.05")
lines(p, c_bonf, lwd = 2, lty = 4, col = "purple")
lines(p, c_t, lwd = 2, lty = 2, col = "steelblue")
grid()
legend("topleft", bty = "n", legend = c("T^2 intervals", "Bonferroni, m = p", "individual t"),
       col = c("darkorange", "purple", "steelblue"), lty = c(1, 4, 2), lwd = 2)
