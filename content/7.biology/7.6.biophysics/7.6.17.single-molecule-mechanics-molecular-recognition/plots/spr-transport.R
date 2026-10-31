# SPR with mass-transport limitation: simulate the two-compartment model and fit a simple 1:1 model (base R).
set.seed(0)
kon <- 1e6; koff <- 1e-3; Rmax <- 100; tinj <- 300; tend <- 900; kt <- 1e8
t <- seq(0, tend, by = 2); dt <- 0.05
concs <- c(3e-9, 10e-9, 30e-9)
sensorgram <- function(C) {           # Euler integration of the quasi-steady two-compartment model
  R <- 0; out <- numeric(length(t)); j <- 1
  for (s in seq(0, tend, by = dt)) {
    if (j <= length(t) && abs(s - t[j]) < dt / 2) { out[j] <- R; j <- j + 1 }
    c <- if (s < tinj) C else 0
    R <- R + dt * (kon * c * (Rmax - R) - koff * R) / (1 + kon * (Rmax - R) / kt)
  }
  out
}
data <- lapply(concs, function(C) sensorgram(C) + rnorm(length(t), 0, 0.3))
simple <- function(p, C) {
  ka <- p[1]; kd <- p[2]; Rm <- p[3]; kobs <- ka * C + kd; Req <- Rm * ka * C / kobs
  Rt <- Req * (1 - exp(-kobs * pmin(t, tinj)))
  Rend <- Req * (1 - exp(-kobs * tinj))
  ifelse(t < tinj, Rt, Rend * exp(-kd * (t - tinj)))
}
ss <- function(lp) { p <- c(exp(lp[1]), exp(lp[2]), lp[3])
  sum(sapply(seq_along(concs), function(i) sum((simple(p, concs[i]) - data[[i]])^2))) }
fit <- optim(c(log(5e5), log(2e-3), 90), ss, control = list(maxit = 5000, reltol = 1e-12))
p <- c(exp(fit$par[1]), exp(fit$par[2]), fit$par[3])
cat(sprintf("1:1 fit: kon = %.3g /M/s, koff = %.3g /s, KD = %.3g nM, Rmax = %.1f RU\n", p[1], p[2], p[2] / p[1] * 1e9, p[3]))
matplot(t, do.call(cbind, data), pch = ".", col = 1:3, xlab = "time / s", ylab = "response / RU")
for (i in seq_along(concs)) lines(t, simple(p, concs[i]), col = i)
