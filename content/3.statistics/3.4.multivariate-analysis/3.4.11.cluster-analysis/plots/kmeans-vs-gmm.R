# k-means versus a Gaussian mixture fitted by EM on elongated clusters, and BIC against the number of components.
library(mclust)

set.seed(0)
band <- matrix(rnorm(800), ncol = 2) %*% diag(c(2.0, 0.3))
blob <- matrix(rnorm(400), ncol = 2) * 0.6
X <- rbind(band[1:200, ],
           sweep(band[201:400, ], 2, c(0, 2.2), "+"),
           sweep(blob, 2, c(7, 1.1), "+"))

km <- kmeans(X, centers = 3, nstart = 10)
bic <- mclustBIC(X, G = 1:7, modelNames = "VVV")  # unconstrained covariance matrices
gm <- Mclust(X, G = 3, modelNames = "VVV")

cols <- c("steelblue", "darkorange", "forestgreen")
pchs <- c(19, 17, 15)
layout(matrix(1:3, 1), widths = c(1.3, 1.3, 1))
plot(X, col = cols[km$cluster], pch = pchs[km$cluster], cex = 0.5, xlab = "x1", ylab = "x2",
     main = "k-means, k = 3")
plot(X, col = cols[gm$classification], pch = pchs[gm$classification], cex = 0.5, xlab = "x1", ylab = "",
     main = "Gaussian mixture (EM), k = 3")
tt <- seq(0, 2 * pi, length.out = 200)
for (g in 1:3) {
  e <- eigen(gm$parameters$variance$sigma[, , g], symmetric = TRUE)
  for (r in 1:2) {
    ell <- gm$parameters$mean[, g] + r * e$vectors %*% (sqrt(e$values) * rbind(cos(tt), sin(tt)))
    lines(ell[1, ], ell[2, ])
  }
}
# mclust reports BIC = 2 ln L - m ln n; flip the sign to match -2 ln L + m ln n.
plot(1:7, -bic[, "VVV"], type = "b", pch = 19, col = "firebrick",
     xlab = "number of components k", ylab = "BIC = -2 ln L + m ln n", main = "Model selection by BIC")
grid()
