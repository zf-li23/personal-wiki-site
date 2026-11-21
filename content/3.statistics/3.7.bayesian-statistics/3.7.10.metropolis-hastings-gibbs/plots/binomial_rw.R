# Random-walk Metropolis for the binomial model with a Beta(1/2, 1/2) prior, n = 10, y = 3.
set.seed(0)
n <- 10; y <- 3
log_q <- function(theta) {
  if (theta <= 0 || theta >= 1) return(-Inf)
  (y - 0.5) * log(theta) + (n - y - 0.5) * log(1 - theta)
}
K <- 10000
samps <- numeric(K); samps[1] <- 0.5
for (t in 1:(K - 1)) {
  cand <- rnorm(1, samps[t], 0.4)
  if (log(runif(1)) < log_q(cand) - log_q(samps[t])) {
    samps[t + 1] <- cand
  } else {
    samps[t + 1] <- samps[t]
  }
}
rate <- length(unique(samps)) / K   # acceptance rate

par(mfrow = c(1, 2))
plot(samps[1:1000], type = "l", xlab = "iteration", ylab = "theta",
     main = sprintf("Trace (acceptance rate %.2f)", rate))
hist(samps, breaks = 40, freq = FALSE, xlab = "theta", main = "Histogram of 10000 draws")
curve(dbeta(x, y + 0.5, n - y + 0.5), add = TRUE, lwd = 2)
