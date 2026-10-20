# Linear PCA versus Gaussian-kernel PCA on two concentric rings.
set.seed(0)
n_per <- 150
theta <- runif(2 * n_per, 0, 2 * pi)
r <- c(rnorm(n_per, 1.0, 0.1), rnorm(n_per, 3.0, 0.15))
x <- cbind(r * cos(theta), r * sin(theta))
label <- rep(1:2, each = n_per)
n <- nrow(x)

# Linear PCA
lin <- prcomp(x)$x

# Gaussian kernel PCA: eigen-decomposition of the doubly centered kernel matrix.
# (kernlab::kpca(x, kernel = "rbfdot", kpar = list(sigma = 1 / (2 * sigma^2))) gives the same scores up to sign and scale.)
sigma <- 1.0
K <- exp(-as.matrix(dist(x))^2 / (2 * sigma^2))
H <- diag(n) - matrix(1 / n, n, n)
e <- eigen(H %*% K %*% H, symmetric = TRUE)
kp <- e$vectors[, 1:2] %*% diag(sqrt(e$values[1:2]))

cols <- c("steelblue", "darkorange")
par(mfrow = c(1, 3))
plot(x, col = cols[label], pch = 19, cex = 0.5, asp = 1, xlab = "x_1", ylab = "x_2", main = "original data")
legend("topright", bty = "n", legend = c("inner ring", "outer ring"), col = cols, pch = 19, cex = 0.8)
plot(lin, col = cols[label], pch = 19, cex = 0.5, asp = 1, xlab = "PC 1", ylab = "PC 2", main = "linear PCA")
plot(kp, col = cols[label], pch = 19, cex = 0.5, xlab = "kernel PC 1", ylab = "kernel PC 2",
     main = "Gaussian kernel PCA (sigma = 1)")
