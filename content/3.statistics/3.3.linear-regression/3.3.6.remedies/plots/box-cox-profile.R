# Box-Cox procedure on simulated data whose spread shrinks with the predictor.
library(MASS)
set.seed(4)
age <- rep(0:4, each = 5)
y <- (0.22 + 0.06 * age + 0.02 * rnorm(length(age)))^-2

op <- par(mfrow = c(1, 3))
plot(age, y, pch = 19, col = "steelblue", xlab = "X", ylab = "Y",
     main = "original scale: spread shrinks with X")
plot(age, y^-0.5, pch = 19, col = "forestgreen", xlab = "X", ylab = "Y^(-1/2)",
     main = "after Y' = Y^(-1/2)")

# profile log-likelihood of lambda with its 95% interval (drawn by boxcox)
fit <- lm(y ~ age, y = TRUE, qr = TRUE)
bc <- boxcox(fit, lambda = seq(-1.5, 1, length.out = 251))
lam_hat <- bc$x[which.max(bc$y)]
ci <- range(bc$x[bc$y >= max(bc$y) - qchisq(0.95, 1) / 2])
title(main = sprintf("lambda_hat = %.2f, 95%% CI [%.2f, %.2f]", lam_hat, ci[1], ci[2]))
par(op)
