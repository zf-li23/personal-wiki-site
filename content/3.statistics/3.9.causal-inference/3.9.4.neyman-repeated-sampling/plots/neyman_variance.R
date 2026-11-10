# Randomization distribution, variance estimators and coverage in a fixed finite population.
set.seed(0)
n <- 100; n_t <- 50; n_c <- n - n_t; k_draws <- 4000
z <- qnorm(0.975)
y0 <- rnorm(n)
eta <- rnorm(n)                          # drives the heterogeneity of unit-level effects
assign <- replicate(k_draws, seq_len(n) %in% sample(n, n_t))   # n x k matrix

simulate <- function(y1) {
  t(apply(assign, 2, function(w) {
    st2 <- var(y1[w]); sc2 <- var(y0[!w])
    v_ney <- sc2 / n_c + st2 / n_t
    c(est = mean(y1[w]) - mean(y0[!w]), v_ney = v_ney,
      v_rho1 = v_ney - (sqrt(st2) - sqrt(sc2))^2 / n)
  }))
}
true_var <- function(y1) var(y0) / n_c + var(y1) / n_t - var(y1 - y0) / n

par(mfrow = c(1, 3))
y1 <- y0 + 1 + eta
sim <- simulate(y1); tau_fs <- mean(y1 - y0)
hist(sim[, "est"], breaks = 40, freq = FALSE, col = "lightsteelblue", border = "white",
     xlab = "difference-in-means estimate", main = "Heterogeneous effects (h = 1)")
curve(dnorm(x, tau_fs, sqrt(true_var(y1))), add = TRUE, col = "darkorange", lwd = 2)
curve(dnorm(x, tau_fs, sqrt(mean(sim[, "v_ney"]))), add = TRUE, col = "firebrick", lwd = 2, lty = 2)

hs <- seq(0, 2, length.out = 11)
res <- t(sapply(hs, function(h) {
  y1 <- y0 + 1 + h * eta
  sim <- simulate(y1); tau_fs <- mean(y1 - y0)
  c(true = true_var(y1), ney = mean(sim[, "v_ney"]), rho1 = mean(sim[, "v_rho1"]),
    cover = mean(abs(sim[, "est"] - tau_fs) <= z * sqrt(sim[, "v_ney"])))
}))
matplot(hs, res[, 1:3], type = "l", lty = 1:3, lwd = 2, col = c("darkorange", "firebrick", "darkgreen"),
        xlab = "effect heterogeneity h", ylab = "variance of the estimator",
        main = "Variance and its estimators")
legend("topleft", c("true", "Neyman", "rho = 1"), lty = 1:3, col = c("darkorange", "firebrick", "darkgreen"), bty = "n")
plot(hs, res[, "cover"], type = "b", pch = 19, ylim = c(0.9, 1), col = "firebrick",
     xlab = "effect heterogeneity h", ylab = "coverage of tau_fs",
     main = "Coverage of the 95% Neyman interval")
abline(h = 0.95, lty = 2, col = "gray")
