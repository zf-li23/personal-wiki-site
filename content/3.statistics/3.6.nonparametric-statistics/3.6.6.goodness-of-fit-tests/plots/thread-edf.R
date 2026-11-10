# Thread break points: EDF with the 95% Kolmogorov band, U(0, 6) and the piecewise-linear alternative.
x <- c(0.6, 0.8, 1.1, 1.2, 1.4, 1.7, 1.8, 1.9, 2.2, 2.4, 2.5, 2.9, 3.1, 3.4, 3.4, 3.9, 4.4, 4.9, 5.2, 5.9)
Fn <- ecdf(x)
plot(Fn, xlim = c(0, 6), main = "", xlab = "break point x (cm)", ylab = "cumulative probability",
     verticals = TRUE, do.points = FALSE, col = "steelblue", lwd = 2)
grid <- seq(0, 6, by = 0.01)
lines(grid, pmin(Fn(grid) + 0.294, 1), type = "s", lty = 3, col = "steelblue")
lines(grid, pmax(Fn(grid) - 0.294, 0), type = "s", lty = 3, col = "steelblue")
lines(grid, punif(grid, 0, 6), col = "darkorange", lwd = 2)
lines(grid, ifelse(grid <= 3, grid / 5, 0.2 + 4 * grid / 30), col = "forestgreen", lwd = 2, lty = 2)
ks.test(x, "punif", 0, 6, exact = TRUE)   # D = 0.18333, p-value = 0.4583
