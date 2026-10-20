# Power functions of Z tests for a normal mean (mu0 = 1, sigma^2 = 4, alpha = 0.05).
alpha <- 0.05
mu0 <- 1
sigma <- 2
mu <- seq(-1, 3, length.out = 400)
za2 <- qnorm(1 - alpha / 2)
za <- qnorm(1 - alpha)

two_sided <- function(n) {
  d <- sqrt(n) * (mu0 - mu) / sigma
  1 - pnorm(za2 + d) + pnorm(-za2 + d)
}
one_sided <- function(n) 1 - pnorm(za + sqrt(n) * (mu0 - mu) / sigma)

guides <- function() {
  abline(h = alpha, lty = 2, col = "grey50")
  abline(v = mu0, lty = 3, col = "grey50")
}

op <- par(mfrow = c(1, 2))
cols <- c("steelblue", "darkorange", "darkgreen")
matplot(mu, sapply(c(20, 50, 200), two_sided), type = "l", lty = 1, lwd = 1.8, col = cols,
        ylim = c(-0.02, 1.03), xlab = "mu", ylab = "power",
        main = "Two-sided test |Z| > z_{alpha/2}")
guides()
legend("left", bty = "n", cex = 0.8, legend = paste("n =", c(20, 50, 200)), col = cols, lwd = 1.8)

matplot(mu, cbind(two_sided(50), one_sided(50)), type = "l", lty = 1, lwd = 1.8,
        col = c("firebrick", "steelblue"), ylim = c(-0.02, 1.03), xlab = "mu", ylab = "",
        main = "Two-sided versus one-sided region, n = 50")
guides()
legend("left", bty = "n", cex = 0.8, legend = c("D: |Z| > z_{alpha/2}", "D_2: Z > z_alpha"),
       col = c("firebrick", "steelblue"), lwd = 1.8)
par(op)
