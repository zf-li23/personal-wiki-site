# Posterior of the average effect in the six-unit normal example (model-based imputation).
set.seed(0)
w <- c(0, 1, 0, 1, 0, 1)
y <- c(0, 9.9, 12.4, 3.6, 0, 24.9)          # first six NSW units (earnings, 1000 USD)
n <- length(y); sig_c <- 10; sig_t <- 8; prior_var <- 100^2

post_mu <- function(yg, sig) {
  prec <- length(yg) / sig^2 + 1 / prior_var
  c(mean = sum(yg) / sig^2 / prec, var = 1 / prec)
}
pc <- post_mu(y[w == 0], sig_c); pt <- post_mu(y[w == 1], sig_t)

# Monte Carlo: theta, then missing outcomes, then tau_fs
draws <- 20000
mu_c <- rnorm(draws, pc["mean"], sqrt(pc["var"]))
mu_t <- rnorm(draws, pt["mean"], sqrt(pt["var"]))
y1_mis <- matrix(rnorm(draws * 3, mu_t, sig_t), draws)
y0_mis <- matrix(rnorm(draws * 3, mu_c, sig_c), draws)
tau_fs <- (rowSums(y1_mis) - sum(y[w == 0]) + sum(y[w == 1]) - rowSums(y0_mis)) / n
c(mean = mean(tau_fs), sd = sd(tau_fs))

hist(tau_fs, breaks = 60, freq = FALSE, col = "lightsteelblue", border = "white",
     xlab = "tau_fs", main = "Posterior of the finite-sample effect")
mean0 <- (3 * pt["mean"] - sum(y[w == 0]) + sum(y[w == 1]) - 3 * pc["mean"]) / n
var0 <- (3 * sig_t^2 + 9 * pt["var"] + 3 * sig_c^2 + 9 * pc["var"]) / n^2
curve(dnorm(x, mean0, sqrt(var0)), add = TRUE, col = "darkorange", lwd = 2)
c(tau_sp_mean = unname(pt["mean"] - pc["mean"]), tau_sp_sd = unname(sqrt(pt["var"] + pc["var"])))
