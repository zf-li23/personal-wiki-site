# Varimax rotation of the principal component loadings of the consumer-preference data.
vars <- c("taste", "good buy", "flavor", "snack", "energy")
L <- matrix(c(0.56, 0.82, 0.78, -0.53, 0.65, 0.75, 0.94, -0.10, 0.80, -0.54), ncol = 2, byrow = TRUE,
            dimnames = list(vars, c("F1", "F2")))

rot <- varimax(L, normalize = TRUE, eps = 1e-10)  # Kaiser-normalized varimax
Tm <- rot$rotmat
print(rot$loadings)
angle <- atan2(Tm[2, 1], Tm[1, 1]) * 180 / pi

tt <- seq(0, 2 * pi, length.out = 300)
par(mfrow = c(1, 2))
for (rotated in c(FALSE, TRUE)) {
  plot(L, pch = 19, col = "steelblue", asp = 1, xlim = c(-1.2, 1.35), ylim = c(-1.2, 1.35),
       xlab = "loading on F1", ylab = "loading on F2",
       main = if (rotated) sprintf("varimax: rotated factor axes (angle %.0f deg)", angle) else "unrotated loadings")
  abline(h = 0, v = 0, col = "gray60")
  lines(cos(tt), sin(tt), lty = 3, col = "gray60")
  text(L, labels = vars, pos = c(4, 2, 4, 4, 1), cex = 0.8)
  if (rotated) {
    cols <- c("firebrick", "forestgreen")
    for (j in 1:2) {
      d <- Tm[, j]
      arrows(-0.3 * d[1], -0.3 * d[2], 1.15 * d[1], 1.15 * d[2], col = cols[j], lwd = 1.8, length = 0.1)
      text(1.22 * d[1], 1.22 * d[2], paste0("F", j, "*"), col = cols[j])
    }
  }
}
