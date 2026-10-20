# X ~ N(0,1), Y = S X with an independent random sign S: normal marginals, zero correlation, not jointly normal.
set.seed(0)
n <- 3000
x <- rnorm(n)
s <- sample(c(-1, 1), n, replace = TRUE)
y <- s * x
z1 <- rnorm(n)
z2 <- rnorm(n)

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))
plot(z1, z2, pch = 19, cex = 0.3, col = adjustcolor("steelblue", 0.4), asp = 1,
     xlim = c(-4, 4), ylim = c(-4, 4), xlab = "first coordinate", ylab = "second coordinate",
     main = "independent N(0,1) pair (jointly normal)")
plot(x, y, pch = 19, cex = 0.3, col = adjustcolor("darkorange", 0.4), asp = 1,
     xlim = c(-4, 4), ylim = c(-4, 4), xlab = "first coordinate", ylab = "",
     main = sprintf("(X, SX): corr = %.2f, not jointly normal", cor(x, y)))
par(op)
