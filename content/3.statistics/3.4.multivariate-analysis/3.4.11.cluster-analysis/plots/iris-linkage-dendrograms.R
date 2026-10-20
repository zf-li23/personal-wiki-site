# Dendrograms of the iris data under single, complete, average and Ward linkage.
d <- dist(iris[, 1:4])  # Euclidean distances
par(mfrow = c(2, 2), mar = c(1, 4, 3, 1))
for (method in c("single", "complete", "average", "ward.D2")) {  # ward.D2: Ward's criterion on Euclidean distances
  hc <- hclust(d, method = method)
  h <- hc$height
  nh <- length(h)
  cut_h <- 0.999 * h[nh - 1] + 0.001 * h[nh - 2]  # cut that leaves three clusters
  plot(hc, labels = FALSE, hang = -1, xlab = "", sub = "", ylab = "height",
       main = paste(sub(".D2", "", method, fixed = TRUE), "linkage"))
  abline(h = cut_h, lty = 2)
  rect.hclust(hc, k = 3, border = c("steelblue", "darkorange", "forestgreen"))
  print(table(cluster = cutree(hc, k = 3), species = iris$Species))
}
