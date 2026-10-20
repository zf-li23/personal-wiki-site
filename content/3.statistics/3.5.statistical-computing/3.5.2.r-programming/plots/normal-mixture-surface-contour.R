# Joint density of two iid normal mixtures 0.7 N(0, 1) + 0.3 N(3, 1): surface and contour plots.
p1 <- 0.7
mix <- function(t) p1 * dnorm(t, 0, 1) + (1 - p1) * dnorm(t, 3, 1)
f <- function(x, y) mix(x) * mix(y)       # X and Y are independent

grid <- seq(-3, 6, length.out = 121)
z <- outer(grid, grid, f)                 # density on the grid

set.seed(0)
n <- 500
xs <- ifelse(runif(n) < p1, 0, 3) + rnorm(n)
ys <- ifelse(runif(n) < p1, 0, 3) + rnorm(n)

op <- par(mfrow = c(1, 2))
persp(grid, grid, z, theta = 30, phi = 30, col = "lightblue", shade = 0.5, border = NA,
      xlab = "x", ylab = "y", zlab = "f(x, y)", main = "Surface plot")
plot(xs, ys, pch = 20, cex = 0.5, col = "grey60", asp = 1, xlab = "x", ylab = "y",
     main = "Contour plot")
contour(grid, grid, z, levels = c(0.002, 0.005, 0.01, 0.02, 0.03, 0.05, 0.07), add = TRUE)
par(op)
