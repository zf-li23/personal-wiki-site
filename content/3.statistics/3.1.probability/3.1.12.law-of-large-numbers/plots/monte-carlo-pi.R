# Monte Carlo estimate of pi: random points in the square and the running estimate 4 x (fraction inside the circle).
set.seed(0)
n_max <- 100000
u <- runif(n_max, -1, 1)
v <- runif(n_max, -1, 1)
inside <- u^2 + v^2 <= 1
est <- 4 * cumsum(inside) / seq_len(n_max)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))
i <- 1:2000
plot(u[i], v[i], pch = 19, cex = 0.3, asp = 1, xlab = "u", ylab = "v",
     col = ifelse(inside[i], "darkorange", "steelblue"),
     main = "2000 uniform points in [-1, 1]^2")
th <- seq(0, 2 * pi, length.out = 400)
lines(cos(th), sin(th), col = "gray30")
legend("topright", bty = "n", cex = 0.8, pch = 19, col = c("darkorange", "steelblue"),
       legend = c("I_j = 1", "I_j = 0"))

plot(seq_len(n_max), est, type = "l", log = "x", ylim = c(2.5, 3.8), col = "forestgreen",
     xlab = "number of points n (log scale)", ylab = "4 x (fraction inside)",
     main = "running estimate of pi")
abline(h = pi, lty = 2)
legend("topright", bty = "n", lty = 2, legend = "pi")
par(op)
