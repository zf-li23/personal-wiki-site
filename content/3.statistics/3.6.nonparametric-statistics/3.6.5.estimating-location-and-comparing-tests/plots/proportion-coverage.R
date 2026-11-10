# Exact coverage of nominal 95% Wald, Wilson, Agresti-Coull and Clopper-Pearson intervals, n = 20.
n <- 20; z <- qnorm(0.975); x <- 0:n; ph <- x / n
wald <- cbind(ph - z * sqrt(ph * (1 - ph) / n), ph + z * sqrt(ph * (1 - ph) / n))
ctr <- (ph + z^2 / (2 * n)) / (1 + z^2 / n)
hw <- z / (1 + z^2 / n) * sqrt(ph * (1 - ph) / n + z^2 / (4 * n^2))
wilson <- cbind(ctr - hw, ctr + hw)
nt <- n + z^2; pt <- (x + z^2 / 2) / nt
ac <- cbind(pt - z * sqrt(pt * (1 - pt) / nt), pt + z * sqrt(pt * (1 - pt) / nt))
cp <- t(sapply(x, function(k) binom.test(k, n)$conf.int))
coverage <- function(ci, p) sum(dbinom(x, n, p)[ci[, 1] <= p & p <= ci[, 2]])
grid <- seq(0.005, 0.995, by = 0.001)
cov <- sapply(list(wald, wilson, ac, cp), function(ci) sapply(grid, function(p) coverage(ci, p)))
matplot(grid, cov, type = "l", lty = 1, col = c("firebrick", "steelblue", "forestgreen", "darkorange"),
        ylim = c(0.5, 1), xlab = "true proportion p", ylab = "coverage probability (n = 20)")
abline(h = 0.95, lty = 2)
legend("bottom", c("Wald", "Wilson", "Agresti-Coull", "Clopper-Pearson"), horiz = TRUE, bty = "n",
       col = c("firebrick", "steelblue", "forestgreen", "darkorange"), lwd = 1)
