# Three causal models with the same observational distribution but different effects of do(X = 3)
set.seed(0)
n <- 4000

model_1 <- function(n, x_do = NULL) {
  x <- if (is.null(x_do)) rnorm(n) else rep(x_do, n)
  y <- x + rnorm(n)
  list(x = x, y = y)
}
model_2 <- function(n, x_do = NULL) {
  y <- rnorm(n, 0, sqrt(2))
  x <- if (is.null(x_do)) y / 2 + rnorm(n, 0, sqrt(0.5)) else rep(x_do, n)
  list(x = x, y = y)
}
model_3 <- function(n, x_do = NULL) {
  z <- rnorm(n)
  x <- if (is.null(x_do)) 0.8 * z + rnorm(n, 0, 0.6) else rep(x_do, n)
  y <- 1.25 * z + rnorm(n, 0, sqrt(0.4375))
  list(x = x, y = y)
}

models <- list("Model 1: X -> Y" = model_1, "Model 2: Y -> X" = model_2,
               "Model 3: X <- Z -> Y" = model_3)
op <- par(mfrow = c(2, 3), mar = c(4, 4, 2, 1))
for (name in names(models)) {
  d <- models[[name]](n)
  plot(d$x, d$y, pch = 16, cex = 0.3, col = rgb(0, 0, 1, 0.25),
       xlab = "x", ylab = "y", main = name)
  abline(v = 3, lty = 2, col = "red")
}
grid <- seq(-5, 7, length.out = 300)
for (name in names(models)) {
  y_do <- models[[name]](n, x_do = 3)$y
  hist(y_do, breaks = 50, freq = FALSE, col = "orange", border = NA,
       xlim = c(-5, 7), xlab = "y", main = "do(X = 3) vs given X = 3")
  lines(grid, dnorm(grid, 3, 1), col = "blue", lwd = 2)
}
par(op)

# Observational moments agree across models: Var(X) = 1, Var(Y) = 2, Cov(X, Y) = 1
sapply(models, function(m) { d <- m(1e5); c(var(d$x), var(d$y), cov(d$x, d$y)) })
