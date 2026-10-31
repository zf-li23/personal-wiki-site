# Run-and-tumble chemotaxis in two dimensions with an adapting MWC receptor cluster
# (same model and parameters as run-and-tumble.py), base R.
set.seed(7)
N <- 6; KI <- 18e-3; KA <- 3.0; alpha <- 1.7; m0 <- 1.0
v <- 20; Dr <- 0.1; lam0 <- 1.0; a0 <- 1 / 3; kmeth <- 0.1; dt <- 0.05

act <- function(m, cc) 1 / (1 + exp(N * (alpha * (m0 - m) + log((1 + cc / KI) / (1 + cc / KA)))))
m_adapted <- function(cc) m0 + (log((1 + cc / KI) / (1 + cc / KA)) - log(1 / a0 - 1) / N) / alpha

simulate <- function(ncell, T, L = NA, c0 = 0.1) {
  conc <- if (is.na(L)) function(x) rep(c0, length(x)) else function(x) c0 * exp(x / L)
  x <- numeric(ncell); y <- numeric(ncell); th <- runif(ncell, 0, 2 * pi)
  m <- m_adapted(conc(x))
  steps <- round(T / dt)
  X <- matrix(0, steps, ncell); Y <- matrix(0, steps, ncell)
  for (i in seq_len(steps)) {
    a <- act(m, conc(x))
    m <- m + dt * kmeth * (a0 - a)
    tumble <- runif(ncell) < lam0 * (a / a0)^3 * dt
    turn <- rnorm(ncell, 68, 25) * pi / 180 * sample(c(-1, 1), ncell, replace = TRUE)
    th <- th + ifelse(tumble, turn, 0) + sqrt(2 * Dr * dt) * rnorm(ncell)
    x <- x + (!tumble) * v * cos(th) * dt
    y <- y + (!tumble) * v * sin(th) * dt
    X[i, ] <- x; Y[i, ] <- y
  }
  list(X = X, Y = Y)
}

op <- par(mfrow = c(1, 3))
for (L in c(NA, 500)) {
  s <- simulate(5, 400, L)
  matplot(s$X, s$Y, type = "l", lty = 1, asp = 1, xlab = "x (um)", ylab = "y (um)",
          main = if (is.na(L)) "uniform" else "gradient, L = 0.5 mm")
}
Ls <- c(500, 1000, 2000)
speeds <- numeric(3)
plot(NULL, xlim = c(0, 300), ylim = c(0, 1300), xlab = "time (s)", ylab = "mean displacement (um)")
for (k in 1:3) {
  s <- simulate(400, 300, Ls[k])
  t <- (seq_len(nrow(s$X))) * dt
  mx <- rowMeans(s$X)
  lines(t, mx, col = k)
  speeds[k] <- coef(lm(mx[t > 60] ~ t[t > 60]))[2]
}
legend("topleft", legend = paste("L =", Ls / 1000, "mm"), col = 1:3, lty = 1, bty = "n")
par(op)
print(data.frame(L_mm = Ls / 1000, drift_um_per_s = speeds))
