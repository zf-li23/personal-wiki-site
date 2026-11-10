# Two-sided p-value functions of the sign, Wilcoxon signed-rank and t tests for the 12 differences.
x <- c(-2, 4, 8, 25, -5, 16, 3, 1, 12, 17, 20, 9)
n <- length(x)
p_sign <- function(theta0) {
  k <- min(sum(x > theta0), sum(x < theta0))
  min(1, 2 * pbinom(k, n, 0.5))
}
p_wilcoxon <- function(theta0) wilcox.test(x, mu = theta0, exact = TRUE)$p.value
p_t <- function(theta0) t.test(x, mu = theta0)$p.value

grid <- seq(-8, 28, by = 0.01) + 0.0037   # avoid data values and Walsh averages
p <- cbind(sapply(grid, p_sign), sapply(grid, p_wilcoxon), sapply(grid, p_t))
matplot(grid, p, type = "l", lty = 1, lwd = 2, col = c("steelblue", "darkorange", "forestgreen"),
        xlab = expression("hypothesized median " * theta[0]), ylab = "two-sided p-value")
abline(h = 0.05, lty = 2, col = "grey40")
rug(x)
legend("topright", c("sign test", "Wilcoxon signed-rank test", "t test"),
       col = c("steelblue", "darkorange", "forestgreen"), lwd = 2, bty = "n")
