# Total error of forward and central difference approximations to f'(1) for f = exp.
x0 <- 1
exact <- exp(x0)
h <- 10^seq(-16, 0, by = 0.1)
forward <- (exp(x0 + h) - exp(x0)) / h
central <- (exp(x0 + h) - exp(x0 - h)) / (2 * h)
err_f <- pmax(abs(forward - exact), 1e-17)   # avoid log(0) when the error vanishes
err_c <- pmax(abs(central - exact), 1e-17)

u <- .Machine$double.eps / 2                  # unit roundoff 2^-53
plot(h, err_f, log = "xy", pch = 19, cex = 0.5, col = "steelblue", ylim = c(1e-12, 10),
     xlab = "step h", ylab = "absolute error",
     main = "f(x) = exp(x) at x0 = 1")
points(h, err_c, pch = 15, cex = 0.5, col = "darkorange")
lines(h, exact * h / 2, lty = 2, col = "steelblue")       # truncation error, forward
lines(h, exact * h^2 / 6, lty = 2, col = "darkorange")    # truncation error, central
lines(h, 2 * u * exact / h, lty = 3, col = "grey40")      # rounding error
abline(v = c(sqrt(4 * u), (3 * u)^(1 / 3)), col = c("steelblue", "darkorange"), lwd = 0.8)
legend("top", bty = "n", cex = 0.8, ncol = 2,
       legend = c("forward difference", "central difference", "h f''/2", "h^2 f'''/6", "2u f/h"),
       col = c("steelblue", "darkorange", "steelblue", "darkorange", "grey40"),
       pch = c(19, 15, NA, NA, NA), lty = c(NA, NA, 2, 2, 3))
