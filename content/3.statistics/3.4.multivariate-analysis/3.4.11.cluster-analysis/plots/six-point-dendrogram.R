# Agglomerative clustering of six points with Euclidean distance and centroid linkage.
P <- matrix(c(0, 0, 1, 2, 2, 1, 4, 1, 5.2, 0, 5, 3), ncol = 2, byrow = TRUE)
labels <- c("(0,0)", "(1,2)", "(2,1)", "(4,1)", "(5.2,0)", "(5,3)")
rownames(P) <- labels

# hclust's centroid update is exact for squared Euclidean distances; take square roots of the heights.
hc <- hclust(dist(P)^2, method = "centroid")
hc$height <- sqrt(hc$height)

# Members and centroid of the cluster formed at each merge.
members <- function(i) if (i < 0) -i else c(members(hc$merge[i, 1]), members(hc$merge[i, 2]))
centroids <- t(sapply(seq_len(nrow(hc$merge)), function(i) colMeans(P[members(i), , drop = FALSE])))

par(mfrow = c(1, 2))
plot(P, pch = 19, col = "steelblue", asp = 1, xlim = c(-0.8, 6.3), ylim = c(-0.8, 3.8),
     xlab = "", ylab = "", main = "Points (o) and centroids of merged clusters (x)")
text(P, labels = labels, pos = 3, cex = 0.8)
points(centroids, pch = 4, col = "firebrick")
text(centroids, labels = sprintf("(%.3g,%.3g)", centroids[, 1], centroids[, 2]),
     pos = 1, col = "firebrick", cex = 0.7)
grid()

plot(hc, hang = -1, xlab = "", sub = "", ylab = "centroid distance at merge",
     main = "Dendrogram (cut at height 3 gives 2 clusters)")
abline(h = 3, lty = 2)
rect.hclust(hc, h = 3, border = c("steelblue", "darkorange"))
