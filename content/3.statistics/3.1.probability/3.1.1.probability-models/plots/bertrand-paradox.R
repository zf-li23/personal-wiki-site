# Bertrand's paradox: three ways of drawing a random chord of the unit circle give three probabilities that the chord is longer than sqrt(3).
set.seed(0)
n_draw <- 120
n_sim <- 100000
L <- sqrt(3)

chords_endpoints <- function(n) {
  a <- runif(n, 0, 2 * pi)
  b <- runif(n, 0, 2 * pi)
  cbind(x1 = cos(a), y1 = sin(a), x2 = cos(b), y2 = sin(b))
}

# chord with a given midpoint (mx, my): perpendicular to the radius through the midpoint
chords_from_midpoints <- function(mx, my) {
  d <- sqrt(mx^2 + my^2)
  half <- sqrt(pmax(1 - d^2, 0))
  dd <- ifelse(d > 0, d, 1)
  ux <- -my / dd
  uy <- mx / dd
  cbind(x1 = mx - half * ux, y1 = my - half * uy, x2 = mx + half * ux, y2 = my + half * uy)
}

chords_radius <- function(n) {
  theta <- runif(n, 0, 2 * pi)
  r <- runif(n, 0, 1)
  chords_from_midpoints(r * cos(theta), r * sin(theta))
}

chords_disk <- function(n) {
  r <- sqrt(runif(n, 0, 1))
  theta <- runif(n, 0, 2 * pi)
  chords_from_midpoints(r * cos(theta), r * sin(theta))
}

methods <- list(
  list(name = "(1) random endpoints", gen = chords_endpoints, exact = "1/3"),
  list(name = "(2) random point on a radius", gen = chords_radius, exact = "1/2"),
  list(name = "(3) random midpoint in the disk", gen = chords_disk, exact = "1/4")
)

op <- par(mfrow = c(1, 3), mar = c(1, 1, 4, 1))
phi <- seq(0, 2 * pi, length.out = 400)
for (m in methods) {
  ch <- m$gen(n_sim)
  long <- sqrt((ch[, "x2"] - ch[, "x1"])^2 + (ch[, "y2"] - ch[, "y1"])^2) >= L
  plot(cos(phi), sin(phi), type = "l", lwd = 1.2, asp = 1, axes = FALSE, xlab = "", ylab = "",
       xlim = c(-1.08, 1.08), ylim = c(-1.08, 1.08), cex.main = 0.95,
       main = sprintf("%s\nexact %s, simulated %.3f", m$name, m$exact, mean(long)))
  i <- seq_len(n_draw)
  segments(ch[i, "x1"], ch[i, "y1"], ch[i, "x2"], ch[i, "y2"], lwd = 0.6,
           col = ifelse(long[i], "steelblue", "darkorange"))
}
legend("bottomleft", bty = "n", cex = 0.8, lty = 1, col = c("steelblue", "darkorange"),
       legend = c("length >= sqrt(3)", "length < sqrt(3)"))
par(op)
