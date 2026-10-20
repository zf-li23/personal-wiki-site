# Scatter plots for several correlation coefficients, plus two nonlinear dependences with zero correlation.
set.seed(0)
n <- 500
op <- par(mfrow = c(2, 3), mar = c(4, 4, 2.5, 1))
for (rho in c(-0.8, 0, 0.5, 0.95)) {
  z1 <- rnorm(n)
  z2 <- rnorm(n)
  x <- z1
  y <- rho * z1 + sqrt(1 - rho^2) * z2
  plot(x, y, pch = 19, cex = 0.4, col = adjustcolor("steelblue", 0.5),
       main = sprintf("rho = %s, sample r = %.2f", rho, cor(x, y)))
}

theta <- runif(n, 0, 2 * pi)
r <- sqrt(runif(n))
x <- r * cos(theta)
y <- r * sin(theta)
plot(x, y, pch = 19, cex = 0.4, col = adjustcolor("darkorange", 0.5),
     main = sprintf("uniform on disk, r = %.2f", cor(x, y)))

x <- rnorm(n)
y <- x^2 + 0.2 * rnorm(n)
plot(x, y, pch = 19, cex = 0.4, col = adjustcolor("darkorange", 0.5),
     main = sprintf("Y = X^2 + noise, r = %.2f", cor(x, y)))
par(op)
