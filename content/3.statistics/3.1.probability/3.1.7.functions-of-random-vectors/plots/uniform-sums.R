# Exact density of S_n = sum of n iid U(-1,1) variables versus the normal approximation N(0, n/3).
exact_density <- function(x, n) {
  total <- numeric(length(x))
  for (k in 0:n) {
    term <- n + x - 2 * k
    total <- total + ifelse(term > 0, (-1)^k * choose(n, k) * pmax(term, 0)^(n - 1), 0)
  }
  ifelse(abs(x) <= n, total / (2^n * factorial(n - 1)), 0)
}

op <- par(mfrow = c(2, 3), mar = c(4, 4, 2.5, 1))
for (n in c(1, 2, 3, 4, 6, 10)) {
  x <- seq(-n - 0.5, n + 0.5, length.out = 800)
  f <- exact_density(x, n)
  g <- dnorm(x, 0, sqrt(n / 3))
  plot(x, f, type = "l", lwd = 1.8, col = "steelblue", ylim = c(0, max(f, g)),
       xlab = "x", ylab = "", main = paste("n =", n))
  lines(x, g, lwd = 1.3, lty = 2, col = "firebrick")
  if (n == 1) {
    legend("topright", bty = "n", cex = 0.8, lty = c(1, 2), col = c("steelblue", "firebrick"),
           legend = c("exact", "N(0, n/3)"))
  }
}
par(op)
