# Hidden extrapolation: a point inside the marginal ranges of X1 and X2 but outside their joint region.
library(MASS)
set.seed(0)
n <- 60
z <- mvrnorm(n, mu = c(0, 0), Sigma = matrix(c(1, 0.85, 0.85, 1), 2))
x1 <- 50 + 10 * z[, 1]
x2 <- 20 + 4 * z[, 2]

# 95% ellipse of the fitted normal distribution as the joint region of the data
m <- c(mean(x1), mean(x2))
eig <- eigen(cov(cbind(x1, x2)))
ang <- seq(0, 2 * pi, length.out = 300)
ell <- eig$vectors %*% (rbind(cos(ang), sin(ang)) * sqrt(5.99 * eig$values)) + m

new <- c(min(x1) + 0.2 * diff(range(x1)), min(x2) + 0.85 * diff(range(x2)))

# the check used in practice: leverage of x_h compared with the largest leverage in the data
X <- cbind(1, x1, x2)
xh <- c(1, new)
h_new <- drop(t(xh) %*% solve(crossprod(X)) %*% xh)
h_max <- max(hatvalues(lm(rnorm(n) ~ x1 + x2)))   # leverages depend on X only

plot(x1, x2, pch = 19, col = adjustcolor("steelblue", 0.75), xlab = "X1", ylab = "X2",
     xlim = range(x1, ell[1, ]), ylim = range(x2, ell[2, ]),
     main = sprintf("Hidden extrapolation: h_new = %.2f > max h_ii = %.2f", h_new, h_max))
lines(ell[1, ], ell[2, ], col = "forestgreen", lwd = 1.8)
rect(min(x1), min(x2), max(x1), max(x2), border = "darkorange", lty = 2)
points(new[1], new[2], pch = 8, cex = 2, lwd = 2, col = "firebrick")
legend("bottomright", bty = "n", cex = 0.8,
       pch = c(19, NA, NA, 8), lty = c(NA, 1, 2, NA), col = c("steelblue", "forestgreen", "darkorange", "firebrick"),
       legend = c("observed cases", "region covered jointly", "ranges of X1 and X2", "new x_h"))
