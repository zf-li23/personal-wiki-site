# Rank-k PCA reconstruction of a synthetic grayscale image (rows as observations, columns as variables).
set.seed(0)
h <- 120
w <- 160
yy <- matrix(0:(h - 1), h, w)
xx <- matrix(0:(w - 1), h, w, byrow = TRUE)
img <- 0.3 + 0.2 * sin(xx / 9.0) * cos(yy / 13.0)
img <- img + 0.5 * (((xx - 50)^2 + (yy - 60)^2) < 28^2)                  # disk
img <- img + 0.4 * ((abs(xx - 115) < 25) & (abs(yy - 45) < 18))         # rectangle
img <- img + 0.35 * ((yy > 80) & (xx > 95) & (yy - 80 < (xx - 95) * 0.6))  # triangle
img <- img + 0.05 * matrix(rnorm(h * w), h, w)

col_mean <- colMeans(img)
Xc <- sweep(img, 2, col_mean)
sv <- svd(Xc)
cum <- cumsum(sv$d^2) / sum(sv$d^2)

reconstruct <- function(k) {
  Uk <- sv$u[, 1:k, drop = FALSE]
  Vk <- sv$v[, 1:k, drop = FALSE]
  sweep(Uk %*% (sv$d[1:k] * t(Vk)), 2, col_mean, "+")
}

# Draw a matrix as an image with row 1 at the top.
show_img <- function(m, main) {
  m <- pmin(pmax(m, min(img)), max(img))
  image(t(m[nrow(m):1, ]), col = gray.colors(256, start = 0, end = 1), zlim = range(img),
        axes = FALSE, asp = h / w, main = main)
}

layout(matrix(c(1, 2, 3, 4, 5, 5, 5, 5), 2, 4, byrow = TRUE))
for (k in c(1, 5, 20)) {
  show_img(reconstruct(k), sprintf("k = %d (%.0f%% of variance)", k, 100 * cum[k]))
}
show_img(img, "original")
plot(1:60, cum[1:60], type = "b", pch = 19, cex = 0.5, col = "steelblue", ylim = c(0, 1.02),
     xlab = "number of principal components k", ylab = "cumulative proportion")
grid()
