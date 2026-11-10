# Smoothing splines with three amounts of smoothing (spar), and the choice by generalized
# cross-validation.
set.seed(42)
x <- seq(1900, 2025, length.out = 80)
y <- 14 + 1.2 * (x - 1900) / (40 + (x - 1900)) + sin(x / 2) * 0.15 + rnorm(length(x), sd = 0.08)
plot(x, y, pch = 16, col = "grey55", xlab = "year", ylab = "annual mean temperature (C)")
cols <- c("darkorange", "steelblue", "forestgreen")
spars <- c(0.2, 0.7, 1.5)
for (k in 1:3) lines(predict(smooth.spline(x, y, spar = spars[k]), seq(1900, 2025, length.out = 400)),
                     col = cols[k], lwd = 2)
abline(lm(y ~ x), lty = 3)
fit_gcv <- smooth.spline(x, y)          # lambda chosen by GCV
fit_gcv$df                              # effective degrees of freedom
legend("topleft", paste("spar =", spars), col = cols, lwd = 2, bty = "n")
