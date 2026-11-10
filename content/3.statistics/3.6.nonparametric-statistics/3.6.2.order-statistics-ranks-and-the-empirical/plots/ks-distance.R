# Kolmogorov distance between an EDF and a CDF, and its distribution-free null distribution.
ksdist <- function(x, CDF, ...) {
  sortx <- sort(x); n <- length(x)
  distup <- (1:n) / n - CDF(sortx, ...)
  distdown <- CDF(sortx, ...) - (0:(n - 1)) / n
  max(pmax(distup, distdown))
}
set.seed(10)
par(mfrow = c(1, 2))
x <- rexp(100)
plot(ecdf(x), verticals = TRUE, do.points = FALSE, main = "Exponential sample, n = 100")
curve(pexp(x), add = TRUE, col = "red")
ksdist(x, pexp)                         # same as ks.test(x, "pexp")$statistic

n <- 20; nrep <- 10000
sims <- list(normal = function() ksdist(rnorm(n), pnorm),
             exponential = function() ksdist(rexp(n), pexp),
             beta = function() ksdist(rbeta(n, 2, 5), pbeta, 2, 5),
             gamma = function() ksdist(rgamma(n, 3), pgamma, 3))
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")
plot(NA, xlim = c(0, 2.2), ylim = c(0, 1), xlab = "sqrt(n) D_n", ylab = "cumulative proportion",
     main = "Null distribution of sqrt(n) D_n, n = 20")
for (k in seq_along(sims)) {
  d <- replicate(nrep, sims[[k]]())
  lines(ecdf(sqrt(n) * d), col = cols[k], do.points = FALSE, verticals = TRUE)
}
legend("bottomright", names(sims), col = cols, lwd = 2, bty = "n")
