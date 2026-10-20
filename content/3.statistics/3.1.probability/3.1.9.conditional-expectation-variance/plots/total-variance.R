# Law of total variance: within-group variance plus between-group variance of the group means.
set.seed(0)
probs <- c(0.1, 0.6, 0.3)
means <- c(165, 175, 180)
sds <- c(4, 5, 4.5)
n <- 6000
g <- sample(1:3, n, replace = TRUE, prob = probs)
x <- rnorm(n, means[g], sds[g])

mu <- sum(probs * means)
within <- sum(probs * sds^2)               # E Var(X | Y)
between <- sum(probs * (means - mu)^2)     # Var E(X | Y)

bins <- seq(145, 200, length.out = 70)
keep <- x >= 145 & x <= 200
cols <- c("steelblue", "darkorange", "forestgreen")
h_all <- hist(x[keep], breaks = bins, plot = FALSE)
plot(h_all, col = NA, border = NA, xlab = "x (height)", ylab = "count", cex.main = 0.9,
     main = sprintf("Var X = %.2f (E Var(X|Y)) + %.2f (Var E(X|Y)) = %.2f; sample variance %.2f",
                    within, between, within + between, var(x)))
for (k in 1:3) {
  plot(hist(x[keep & g == k], breaks = bins, plot = FALSE), add = TRUE,
       col = adjustcolor(cols[k], 0.45), border = NA)
}
plot(h_all, add = TRUE, col = NA, border = "gray40")
abline(v = mu, col = "firebrick", lty = 2, lwd = 1.5)
legend("topleft", bty = "n", cex = 0.8, pch = c(15, 15, 15, NA), lty = c(NA, NA, NA, 1),
       col = c(adjustcolor(cols, 0.45), "gray40"),
       legend = c(sprintf("group y = %d: mean %.0f", 24:26, means), "all"))
