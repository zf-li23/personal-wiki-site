# Power of Fisher's exact test for three statistics under three outcome models.
set.seed(0)
n <- 100; n_t <- 50
alpha <- 0.10; k_draws <- 300; reps <- 300
ref <- replicate(k_draws, sample(n, n_t))          # treated indices of reference assignments

p_values <- function(y_obs, w_obs) {
  r <- rank(y_obs) - (n + 1) / 2
  stat <- function(tr, kind) {
    v <- if (kind == "rank") r else y_obs
    if (kind == "median") abs(median(v[tr]) - median(v[-tr])) else abs(mean(v[tr]) - mean(v[-tr]))
  }
  tr_obs <- which(w_obs)
  sapply(c("mean", "median", "rank"), function(kind) {
    t_obs <- stat(tr_obs, kind)
    t_ref <- apply(ref, 2, stat, kind = kind)
    (1 + sum(t_ref >= t_obs - 1e-12)) / (k_draws + 1)
  })
}

draw_y0 <- function(model) {
  if (model == "outliers") {
    y0 <- rnorm(n); bad <- runif(n) < 0.1; y0[bad] <- rnorm(sum(bad), 0, 5); y0
  } else if (model == "multiplicative") exp(rnorm(n)) else rnorm(n)
}

taus <- seq(0, 0.8, length.out = 9)
par(mfrow = c(1, 3))
for (model in c("normal", "outliers", "multiplicative")) {
  power <- t(sapply(taus, function(tau) {
    rej <- replicate(reps, {
      y0 <- draw_y0(model)
      y1 <- if (model == "multiplicative") y0 * exp(tau) else y0 + tau
      w_obs <- seq_len(n) %in% sample(n, n_t)
      p_values(ifelse(w_obs, y1, y0), w_obs) <= alpha
    })
    rowMeans(rej)
  }))
  matplot(taus, power, type = "l", lty = 1:3, lwd = 2, col = 1:3, ylim = c(0, 1),
          xlab = "effect size tau", ylab = "power at level 0.1", main = model)
  abline(h = alpha, col = "gray")
  if (model == "normal") legend("topleft", c("mean", "median", "rank"), lty = 1:3, col = 1:3, bty = "n")
}
