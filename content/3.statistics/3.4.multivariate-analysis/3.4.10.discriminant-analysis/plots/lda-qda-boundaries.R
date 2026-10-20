# LDA versus QDA decision boundaries for two simulated normal populations with unequal covariance matrices.
library(MASS)

set.seed(0)
mu1 <- c(0.0, 0.0)
mu2 <- c(2.0, 1.5)
S1 <- matrix(c(1.0, 0.6, 0.6, 1.0), 2, 2)
S2 <- matrix(c(0.3, -0.1, -0.1, 2.0), 2, 2)
n <- 150
X <- rbind(mvrnorm(n, mu1, S1), mvrnorm(n, mu2, S2))
colnames(X) <- c("x1", "x2")
y <- factor(rep(1:2, each = n))

gx <- seq(-3.5, 5, length.out = 400)
gy <- seq(-3.5, 5.5, length.out = 400)
grid_pts <- as.matrix(expand.grid(x1 = gx, x2 = gy))

cols <- c("steelblue", "darkorange")
par(mfrow = c(1, 2))
for (name in c("LDA", "QDA")) {
  fit <- if (name == "LDA") lda(X, grouping = y) else qda(X, grouping = y)
  z <- matrix(predict(fit, grid_pts)$posterior[, 2], length(gx), length(gy))
  err <- mean(predict(fit, X)$class != y)  # apparent error rate
  image(gx, gy, z, breaks = c(0, 0.5, 1), col = adjustcolor(cols, 0.15),
        xlab = "x1", ylab = "x2", main = sprintf("%s (apparent error rate %.3f)", name, err))
  contour(gx, gy, z, levels = 0.5, drawlabels = FALSE, lwd = 1.5, add = TRUE)
  points(X, col = cols[y], pch = c(19, 17)[y], cex = 0.6)
}
legend("topleft", bty = "n", cex = 0.8, legend = c("population 1", "population 2"), col = cols, pch = c(19, 17))
