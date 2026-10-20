# Classical MDS of road distances (km) between eight cities in eastern China.
cities <- c("Beijing", "Tianjin", "Jinan", "Qingdao", "Zhengzhou", "Shanghai", "Hangzhou", "Nanjing")
lower <- list(0, c(118, 0), c(439, 363, 0), c(668, 571, 362, 0), c(714, 729, 443, 772, 0),
              c(1259, 1145, 886, 776, 984, 0), c(1328, 1191, 872, 828, 962, 203, 0),
              c(1065, 936, 626, 617, 710, 322, 305, 0))
n <- length(cities)
D <- matrix(0, n, n, dimnames = list(cities, cities))
for (i in seq_len(n)) {
  for (j in seq_along(lower[[i]])) {
    D[i, j] <- D[j, i] <- lower[[i]][j]
  }
}

fit <- cmdscale(D, k = 2, eig = TRUE)  # eigen-decomposition of B = -H D^2 H / 2
lam <- fit$eig
Z <- fit$points

# CMDS fixes the configuration only up to an orthogonal transformation; choose the one
# (rotation and/or reflection) that best matches approximate map positions (longitude, latitude).
lonlat <- matrix(c(116.4, 39.9, 117.2, 39.1, 117.0, 36.7, 120.4, 36.1, 113.6, 34.7,
                   121.5, 31.2, 120.2, 30.3, 118.8, 32.1), ncol = 2, byrow = TRUE)
target <- sweep(sweep(lonlat, 2, colMeans(lonlat)), 2, c(111 * cos(35 * pi / 180), 111), "*")
s <- svd(t(Z) %*% target)
Z <- Z %*% (s$u %*% t(s$v))

layout(matrix(1:2, 1), widths = c(1, 1.4))
barplot(lam / 1e3, names.arg = 1:n, col = ifelse(lam > 0, "steelblue", "firebrick"),
        xlab = "index i", ylab = "eigenvalue of B (1000 km^2)", main = "eigenvalues of B")
abline(h = 0, col = "gray")

plot(Z, pch = 19, col = "steelblue", asp = 1,
     xlim = range(Z[, 1]) + c(-150, 250), ylim = range(Z[, 2]) + c(-100, 100),
     xlab = "coordinate 1 (km)", ylab = "coordinate 2 (km)",
     main = "two-dimensional CMDS configuration (oriented)")
text(Z, labels = cities, pos = ifelse(cities == "Hangzhou", 1, 4), cex = 0.8)
