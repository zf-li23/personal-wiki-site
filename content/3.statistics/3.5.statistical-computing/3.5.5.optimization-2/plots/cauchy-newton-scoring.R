# Cauchy location log-likelihood: Newton-Raphson versus Fisher scoring.
x <- c(1.77, -0.23, 2.76, 3.80, 3.47, 56.75, -1.34, 4.24, -2.44, 3.29,
       3.71, -2.40, 4.53, -0.07, -1.05, -13.87, -2.53, -1.75, 0.27, 43.21)
n <- length(x)
loglik <- function(t) -sum(log(1 + (x - t)^2)) - n * log(pi)
score <- function(t) sum(2 * (x - t) / (1 + (x - t)^2))
obs_info <- function(t) 2 * sum((1 - (x - t)^2) / (1 + (x - t)^2)^2)  # J(theta) = -l''

newton <- function(t, k) {
  path <- t
  for (i in 1:k) { t <- t + score(t) / obs_info(t); path <- c(path, t) }
  path
}
scoring <- function(t, k) {
  path <- t
  for (i in 1:k) { t <- t + score(t) / (n / 2); path <- c(path, t) }  # I(theta) = n/2
  path
}

mle <- tail(newton(-0.2, 50), 1)
op <- par(mfrow = c(1, 2))
grid <- seq(-20, 60, length.out = 4000)
plot(grid, sapply(grid, loglik), type = "l", col = "steelblue",
     xlab = "theta", ylab = "log-likelihood", main = sprintf("MLE = %.4f", mle))
p1 <- newton(1.5, 30); p2 <- newton(7, 30); p3 <- scoring(7, 30)
points(p1[1:6], sapply(p1[1:6], loglik), type = "b", lty = 2, col = "firebrick", pch = 19)
points(p2[1:6], sapply(p2[1:6], loglik), type = "b", lty = 2, col = "darkgreen", pch = 19)
points(p3[1:8], sapply(p3[1:8], loglik), type = "b", lty = 3, col = "darkorange", pch = 15)
abline(v = mle, lty = 2, col = "gray")
legend("bottomleft", bty = "n", cex = 0.8, col = c("firebrick", "darkgreen", "darkorange"),
       pch = c(19, 19, 15),
       legend = sprintf(c("Newton from 1.5 -> %.2f", "Newton from 7 -> %.2f", "scoring from 7 -> %.2f"),
                        c(tail(p1, 1), tail(p2, 1), tail(p3, 1))))

k <- 25
e_nr <- abs(newton(-1, k) - mle); e_fs <- abs(scoring(-1, k) - mle)
e_nr[e_nr < 1e-16] <- NA
plot(0:k, e_fs, log = "y", type = "b", pch = 15, col = "darkorange",
     ylim = range(c(e_nr, e_fs), na.rm = TRUE),
     xlab = "iteration t", ylab = "|theta_t - MLE|", main = "start theta_0 = -1")
lines(0:k, e_nr, type = "b", pch = 19, col = "firebrick")
legend("bottomleft", bty = "n", legend = c("Newton-Raphson", "Fisher scoring"),
       col = c("firebrick", "darkorange"), pch = c(19, 15))
par(op)
