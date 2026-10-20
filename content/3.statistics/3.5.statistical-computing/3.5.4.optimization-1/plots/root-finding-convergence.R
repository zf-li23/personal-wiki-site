# Errors of bisection, fixed-point iterations, the secant method and Newton's method for x + log(x) = 0.
f <- function(x) x + log(x)
df <- function(x) 1 + 1 / x
x_star <- uniroot(f, c(0.1, 1), tol = 1e-15)$root   # 0.5671433, the omega constant

bisection <- function(a, b, n) {
  out <- numeric(n)
  for (t in 1:n) {
    m <- (a + b) / 2; out[t] <- m
    if (f(a) * f(m) <= 0) b <- m else a <- m
  }
  out
}
fixed_point <- function(G, x, n) { out <- numeric(n); for (t in 1:n) { x <- G(x); out[t] <- x }; out }
secant <- function(x0, x1, n) {
  out <- c()
  for (t in 1:n) {
    if (f(x1) == f(x0)) break
    x2 <- x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)); x0 <- x1; x1 <- x2; out <- c(out, x1)
  }
  out
}
newton <- function(x, n) { out <- numeric(n); for (t in 1:n) { x <- x - f(x) / df(x); out[t] <- x }; out }

n <- 40
runs <- list("bisection on [0.1, 1]" = bisection(0.1, 1, n),
             "fixed point G2(x) = exp(-x)" = fixed_point(function(x) exp(-x), 1, n),
             "fixed point G3(x) = (x + exp(-x))/2" = fixed_point(function(x) (x + exp(-x)) / 2, 1, n),
             "secant from 1, 0.9" = secant(1, 0.9, n),
             "Newton from 1" = newton(1, n))
cols <- c("blue", "orange", "darkgreen", "purple", "red")
plot(NA, xlim = c(1, n), ylim = c(1e-17, 1), log = "y", xlab = "iteration t", ylab = "|x(t) - x*|",
     main = "Root of f(x) = x + log(x): linear versus superlinear convergence")
for (i in seq_along(runs)) {
  e <- abs(runs[[i]] - x_star); e[e == 0] <- NA
  lines(seq_along(e), e, type = "b", pch = i, cex = 0.6, col = cols[i])
}
legend("topright", names(runs), col = cols, pch = seq_along(runs), lty = 1, cex = 0.8)
