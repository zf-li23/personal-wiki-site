# Estimating a mitotic field from one synthetic section (Section 31.6): raw index, iterated nearest-neighbour
# smoothing inside the tissue, and a Poisson GLM (log link, offset log rho) on 15 cosine functions.
set.seed(7)
nx <- 30; ny <- 22
u <- (seq_len(nx) - 0.5) / nx
v <- (seq_len(ny) - 0.5) / ny
U <- matrix(rep(u, each = ny), ny, nx)
V <- matrix(rep(v, times = nx), ny, nx)
mask <- (U / 0.98)^2.6 + ((V - 0.5) / 0.47)^2 <= 1
core <- exp(-(((U - 0.45) / 0.22)^2 + ((V - 0.5) / 0.2)^2))
m_true <- 0.13 * (1 - 0.5 * core) * (0.75 + 0.25 * U)
rho <- matrix(rpois(nx * ny, 40), ny, nx) * mask
M <- matrix(rpois(nx * ny, m_true * rho), ny, nx) * mask

raw <- ifelse(mask, M / pmax(rho, 1), NA)

shift <- function(A, di, dj) {
  B <- matrix(0, nrow(A), ncol(A))
  ri <- seq_len(nrow(A)); ci <- seq_len(ncol(A))
  si <- ri - di; sj <- ci - dj
  ok_i <- si >= 1 & si <= nrow(A); ok_j <- sj >= 1 & sj <= ncol(A)
  B[ri[ok_i], ci[ok_j]] <- A[si[ok_i], sj[ok_j]]
  B
}
smooth <- function(A, r) {
  for (k in seq_len(r)) {
    A <- 0.5 * A + 0.25 * (shift(A, 1, 0) + shift(A, -1, 0))
    A <- 0.5 * A + 0.25 * (shift(A, 0, 1) + shift(A, 0, -1))
  }
  A
}
sm <- ifelse(mask, smooth(M * mask, 3) / pmax(smooth(rho * mask, 3), 1e-9), NA)

ij <- subset(expand.grid(i = 0:4, j = 0:4), i + j <= 4)
d <- data.frame(M = M[mask], rho = rho[mask])
for (k in seq_len(nrow(ij))) {
  d[[paste0("b", k)]] <- cos(pi * ij$i[k] * U[mask]) * cos(pi * ij$j[k] * V[mask])
}
fit <- glm(as.formula(paste("M ~ 0 +", paste0("b", seq_len(nrow(ij)), collapse = " + "),
                            "+ offset(log(pmax(rho, 1)))")), family = poisson, data = d)
ml <- matrix(NA, ny, nx)
ml[mask] <- exp(predict(fit, type = "link") - log(pmax(d$rho, 1)))

rmse <- function(E) sqrt(mean((E[mask] - m_true[mask])^2))
cat(sprintf("RMSE raw %.3f, smoothed %.3f, Poisson ML %.3f\n", rmse(raw), rmse(sm), rmse(ml)))

op <- par(mfrow = c(1, 4), mar = c(1, 1, 3, 1))
pal <- colorRampPalette(c("white", "#A893DA", "#6E55A8"))(64)
for (F in list(list(ifelse(mask, m_true, NA), "true field"), list(raw, "raw index"), list(sm, "smoothed (r = 3)"),
               list(ml, "Poisson ML, 15 terms"))) {
  image(t(F[[1]]), col = pal, zlim = c(0.03, 0.2), axes = FALSE, main = F[[2]])
}
par(op)
