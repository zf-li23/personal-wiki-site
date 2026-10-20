# Box-Cox transformation for the time between computer failures at three locations.
library(MASS)
y <- c(4.41, 100.65, 14.45, 47.13, 85.21,
       8.24, 81.16, 7.35, 12.29, 1.61,
       106.19, 33.83, 78.88, 342.81, 44.33)
location <- factor(rep(1:3, each = 5))

set.seed(0)
op <- par(mfrow = c(1, 3))
stripchart(y ~ location, vertical = TRUE, method = "jitter", jitter = 0.08, pch = 19, col = "steelblue",
           xlab = "location", ylab = "time between failures", main = "Raw times")

# profile log-likelihood of lambda for the one-way ANOVA model, with its 95% interval
fit <- lm(y ~ location, y = TRUE, qr = TRUE)
bc <- boxcox(fit, lambda = seq(-2, 2, length.out = 801))
lam_hat <- bc$x[which.max(bc$y)]
title(main = sprintf("Box-Cox profile: lambda_hat = %.2f", lam_hat))

stripchart(log(y) ~ location, vertical = TRUE, method = "jitter", jitter = 0.08, pch = 19, col = "forestgreen",
           xlab = "location", ylab = "log time between failures", main = "log(time), lambda = 0")
par(op)
print(anova(lm(log(y) ~ location)))
