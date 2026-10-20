# Mallows' Cp for all subsets of six simulated candidate predictors (three relevant).
library(MASS)
set.seed(0)
n <- 60
k <- 6
Sigma <- 0.3 * matrix(1, k, k) + 0.7 * diag(k)
Z <- mvrnorm(n, mu = rep(0, k), Sigma = Sigma)
y <- 1 + 1.0 * Z[, 1] + 0.8 * Z[, 2] + 0.6 * Z[, 3] + rnorm(n)

sse <- function(cols) {
  X <- cbind(1, Z[, cols, drop = FALSE])
  sum(lm.fit(X, y)$residuals^2)
}

# all 2^6 = 64 subsets (leaps::regsubsets(Z, y, nbest = 20)$cp gives the same Cp values)
subsets <- c(list(integer(0)), unlist(lapply(1:k, function(s) combn(k, s, simplify = FALSE)), recursive = FALSE))
P <- k + 1
mse_full <- sse(1:k) / (n - P)
p <- sapply(subsets, length) + 1
cp <- sapply(subsets, sse) / mse_full - (n - 2 * p)
relevant <- sapply(subsets, function(s) all(1:3 %in% s))
best <- which.min(cp)

plot(p, cp, log = "y", pch = 19, col = ifelse(relevant, "forestgreen", "steelblue"),
     xlab = "number of parameters p", ylab = "Mallows' Cp",
     main = "All 64 subsets: biased models lie far above the line Cp = p")
lines(c(1, P), c(1, P), lty = 2, col = "gray30")
text(p[best] + 0.15, cp[best], paste("smallest Cp: X", paste(subsets[[best]], collapse = ", X"), sep = ""),
     adj = 0, cex = 0.8)
legend("topright", bty = "n", cex = 0.8, pch = c(NA, 19, 19), lty = c(2, NA, NA),
       col = c("gray30", "forestgreen", "steelblue"),
       legend = c("Cp = p", "contains all relevant predictors", "misses a relevant predictor"))
