# Sensitivity curves of the mean, median and Hodges-Lehmann estimate when the largest of the
# 12 differences (25) is replaced by y.
base <- c(-2, 4, 8, -5, 16, 3, 1, 12, 17, 20, 9)
hl <- function(x) { w <- outer(x, x, "+") / 2; median(w[lower.tri(w, diag = TRUE)]) }
ys <- seq(-60, 120, by = 0.25)
est <- t(sapply(ys, function(y) { x <- c(base, y); c(mean(x), median(x), hl(x)) }))
matplot(ys, est, type = "l", lty = 1, lwd = 2, col = c("forestgreen", "steelblue", "darkorange"),
        xlab = "value y of the replaced observation", ylab = "estimate of location")
abline(v = 25, lty = 3)
legend("topleft", c("mean", "median", "Hodges-Lehmann"), col = c("forestgreen", "steelblue", "darkorange"),
       lwd = 2, bty = "n")
