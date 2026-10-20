# Ridge trace and exact bias-variance decomposition of the ridge estimator for collinear predictors.
set.seed(0)
n <- 20
p <- 3
z <- rnorm(n)
X <- cbind(z + 0.08 * rnorm(n), z + 0.08 * rnorm(n), rnorm(n))
# standardize the columns (divisor n, as in the correlation transformation up to a constant)
X <- scale(X, center = TRUE, scale = apply(X, 2, function(v) sqrt(mean((v - mean(v))^2))))
beta <- c(1.0, 0.5, -0.5)
sigma <- 1
lams <- 10^seq(-3, 2, length.out = 201)
XtX <- crossprod(X)

# MASS::lm.ridge(y ~ X, lambda = lams) gives the same trace up to its own scaling of X
ridge <- function(y, lam) solve(XtX + lam * diag(p), crossprod(X, y))
y0 <- drop(X %*% beta + sigma * rnorm(n))
y0 <- y0 - mean(y0)
path <- t(sapply(lams, function(l) ridge(y0, l)))

# exact squared bias and variance for the fixed design
bias2 <- sapply(lams, function(l) {
  A <- solve(XtX + l * diag(p), XtX)
  sum((A %*% beta - beta)^2)
})
vars <- sapply(lams, function(l) {
  M <- solve(XtX + l * diag(p))
  sigma^2 * sum(diag(M %*% XtX %*% M))
})
mse <- bias2 + vars
mse_ols <- sigma^2 * sum(diag(solve(XtX)))

op <- par(mfrow = c(1, 2))
cols <- c("steelblue", "darkorange", "forestgreen")
matplot(lams, path, type = "l", lty = 1, lwd = 1.6, col = cols, log = "x",
        xlab = "lambda (log scale)", ylab = "standardized coefficient", main = "Ridge trace")
abline(h = 0, col = "gray")
legend("topright", bty = "n", cex = 0.8, lwd = 1.6, col = cols,
       legend = c("x1", "x2 (nearly equal to x1)", "x3"))

matplot(lams, cbind(bias2, vars, mse), type = "l", lty = 1, lwd = c(1.6, 1.6, 2),
        col = c("steelblue", "darkorange", "firebrick"), log = "x", ylim = c(0, 1.15 * mse_ols),
        xlab = "lambda (log scale)", ylab = "E ||b_R - beta||^2 components", main = "Bias-variance trade-off")
abline(h = mse_ols, lty = 2, col = "gray")
k <- which.min(mse)
points(lams[k], mse[k], pch = 19, col = "firebrick")
legend("topright", bty = "n", cex = 0.8, lty = c(1, 1, 1, 2), lwd = c(1.6, 1.6, 2, 1),
       col = c("steelblue", "darkorange", "firebrick", "gray"),
       legend = c("squared bias", "variance", "MSE = bias^2 + variance", "MSE of OLS"))
par(op)
