# EM for the genetic linkage multinomial (125, 18, 20, 34): monotone likelihood and linear convergence.
loglik <- function(t) 125 * log(2 + t) + 38 * log(1 - t) + 34 * log(t)
em_step <- function(t) {
  x12 <- 125 * t / (2 + t)            # E-step: expected count in the hidden sub-cell
  (x12 + 34) / (x12 + 34 + 18 + 20)   # M-step
}
path <- 0.05
for (i in 1:40) path <- c(path, em_step(tail(path, 1)))
mle <- tail(path, 1)

# fraction of missing information at the MLE
x12 <- 125 * mle / (2 + mle)
i_com <- (x12 + 34) / mle^2 + 38 / (1 - mle)^2
i_obs <- 125 / (2 + mle)^2 + 38 / (1 - mle)^2 + 34 / mle^2
rate <- (i_com - i_obs) / i_com

op <- par(mfrow = c(1, 2))
curve(loglik, 0.02, 0.98, col = "steelblue",
      xlab = "theta", ylab = "observed log-likelihood", main = sprintf("MLE = %.7f", mle))
points(path[1:6], loglik(path[1:6]), type = "b", lty = 2, pch = 19, col = "firebrick")
abline(v = mle, lty = 2, col = "gray")
err <- abs(path[1:15] - mle)
plot(0:14, err, log = "y", type = "b", pch = 19, col = "firebrick",
     xlab = "iteration t", ylab = "|theta_t - MLE|", main = sprintf("rate = %.4f", rate))
lines(0:14, err[4] * rate^((0:14) - 3), lty = 2, col = "gray")
par(op)
c(mle = mle, rate = rate, se = 1 / sqrt(i_obs))
