# Relative error of four sample-variance algorithms when the data have a large mean.
set.seed(0)
z <- rnorm(1000)

two_pass <- function(x) sum((x - mean(x))^2) / (length(x) - 1)
textbook <- function(x) (sum(x^2) - sum(x)^2 / length(x)) / (length(x) - 1)
west <- function(x) {
  m <- x[1]; t <- 0
  for (k in 2:length(x)) {
    d <- x[k] - m
    m <- m + d / k
    t <- t + (k - 1) * d * d / k
  }
  t / (length(x) - 1)
}
cotton <- function(x) {
  m <- x[1]; t <- 0
  for (k in 2:length(x)) {
    m_old <- m
    m <- m + (x[k] - m) / k
    t <- t + x[k]^2 + (k - 1) * m_old^2 - k * m^2
  }
  t / (length(x) - 1)
}

shifts <- 10^(0:9)
err <- sapply(shifts, function(c) {
  x <- z + c
  ref <- two_pass(x - c)   # reference: the shifted data are recovered almost exactly
  sapply(list(two_pass, west, textbook, cotton), function(f) max(abs(f(x) - ref) / ref, 1e-17))
})
matplot(shifts, t(err), log = "xy", type = "b", pch = c(19, 15, 17, 18), lty = 1,
        col = c("steelblue", "darkorange", "forestgreen", "firebrick"),
        xlab = "mean of the data c", ylab = "relative error of S^2")
abline(h = 1, lty = 3, col = "grey50")
legend("topleft", bty = "n", cex = 0.8, legend = c("two-pass", "West (one pass)", "textbook", "Cotton"),
       col = c("steelblue", "darkorange", "forestgreen", "firebrick"), pch = c(19, 15, 17, 18), lty = 1)
