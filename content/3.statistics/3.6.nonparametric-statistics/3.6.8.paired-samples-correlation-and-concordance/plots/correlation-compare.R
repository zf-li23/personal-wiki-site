# Pearson, Spearman and Kendall coefficients for a linear, a monotone nonlinear
# and an outlier-contaminated sample (random numbers differ from the Python version).
set.seed(0)
n <- 30
x <- sort(runif(n, 0, 3))
y1 <- 1 + x + rnorm(n, 0, 0.6)
y2 <- exp(2 * x)
x3 <- x; y3 <- rnorm(n)
x3[n] <- 12; y3[n] <- 12
coefs <- function(x, y) sapply(c("pearson", "spearman", "kendall"),
                               function(m) round(cor(x, y, method = m), 2))
op <- par(mfrow = c(1, 3))
plot(x, y1, pch = 19, main = paste(coefs(x, y1), collapse = " / "))
plot(x, y2, pch = 19, main = paste(coefs(x, y2), collapse = " / "))
plot(x3, y3, pch = 19, main = paste(coefs(x3, y3), collapse = " / "))
par(op)
print(rbind(linear = coefs(x, y1), monotone = coefs(x, y2), outlier = coefs(x3, y3)))
