# Two-sample T^2 confidence ellipse for mu1 - mu2 (p = 2), with T^2, Bonferroni and one-at-a-time intervals.
library(MASS)

set.seed(0)
p <- 2
n1 <- 30
n2 <- 25
alpha <- 0.05
Sigma <- matrix(c(1.0, 0.7, 0.7, 1.5), 2, 2)
x1 <- mvrnorm(n1, c(1.0, 0.5), Sigma)
x2 <- mvrnorm(n2, c(0.3, 0.2), Sigma)
d <- colMeans(x1) - colMeans(x2)
Sp <- ((n1 - 1) * cov(x1) + (n2 - 1) * cov(x2)) / (n1 + n2 - 2)
V <- (1 / n1 + 1 / n2) * Sp

df <- n1 + n2 - 2
c2 <- df * p / (df - p + 1) * qf(1 - alpha, p, df - p + 1)
c0 <- sqrt(c2)

# Hotelling's two-sample statistic for H0: mu1 = mu2.
T2 <- drop(t(d) %*% solve(V, d))
cat(sprintf("T^2 = %.3f, critical value = %.3f\n", T2, c2))

# Ellipse {delta : (d - delta)^T V^(-1) (d - delta) <= c^2}.
e <- eigen(V, symmetric = TRUE)
tt <- seq(0, 2 * pi, length.out = 400)
ell <- d + c0 * e$vectors %*% (sqrt(e$values) * rbind(cos(tt), sin(tt)))

se <- sqrt(diag(V))
half <- list(c0 * se, qt(1 - alpha / (2 * p), df) * se, qt(1 - alpha / 2, df) * se)
cols <- c("steelblue", "darkorange", "forestgreen")
ltys <- c(2, 4, 3)

plot(ell[1, ], ell[2, ], type = "l", lwd = 2, col = "steelblue", asp = 1,
     xlim = range(ell[1, ], d[1] + c(-1, 1) * half[[1]][1]),
     ylim = range(ell[2, ], d[2] + c(-1, 1) * half[[1]][2]),
     xlab = "delta_1 = mu_11 - mu_21", ylab = "delta_2 = mu_12 - mu_22")
for (i in 1:3) {
  rect(d[1] - half[[i]][1], d[2] - half[[i]][2], d[1] + half[[i]][1], d[2] + half[[i]][2],
       border = cols[i], lty = ltys[i], lwd = 1.5)
}
points(d[1], d[2], pch = 19, col = "firebrick")
abline(h = 0, v = 0, col = "gray", lwd = 0.6)
legend("topleft", bty = "n", cex = 0.75,
       legend = c("95% confidence ellipse", "T^2 simultaneous intervals", "Bonferroni intervals",
                  "one-at-a-time t intervals", "observed mean difference"),
       col = c("steelblue", cols, "firebrick"), lty = c(1, ltys, NA), pch = c(NA, NA, NA, NA, 19))
