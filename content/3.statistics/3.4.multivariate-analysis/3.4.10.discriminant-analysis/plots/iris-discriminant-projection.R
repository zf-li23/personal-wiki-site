# Iris data on the first two sample discriminants versus the first two principal components.
library(MASS)

X <- iris[, 1:4]
y <- iris$Species
Z_lda <- predict(lda(X, grouping = y), X)$x[, 1:2]
Z_pca <- prcomp(X)$x[, 1:2]

cols <- c("steelblue", "darkorange", "forestgreen")
pchs <- c(1, 2, 0)
par(mfrow = c(1, 2))
for (case in list(list(Z = Z_lda, title = "Fisher discriminants", lab = c("first discriminant", "second discriminant")),
                  list(Z = Z_pca, title = "Principal components", lab = c("PC1", "PC2")))) {
  Z <- case$Z
  plot(Z, col = cols[y], pch = pchs[y], cex = 0.8, xlab = case$lab[1], ylab = case$lab[2], main = case$title)
  centers <- apply(Z, 2, function(z) tapply(z, y, mean))
  points(centers, pch = 4, cex = 2.5, lwd = 3, col = cols)
  grid()
}
legend("topright", bty = "n", cex = 0.8, legend = levels(y), col = cols, pch = pchs)
