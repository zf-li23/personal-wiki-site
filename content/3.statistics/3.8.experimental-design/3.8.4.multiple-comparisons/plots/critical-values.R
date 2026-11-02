# Critical values on the |t| scale for all pairwise comparisons: LSD, Tukey, Bonferroni and Scheffe.
nu <- 16; alpha <- 0.05
a <- 2:12
m <- a * (a - 1) / 2
crit <- cbind(LSD = qt(1 - alpha / 2, nu),
              Tukey = qtukey(1 - alpha, a, nu) / sqrt(2),
              Bonferroni = qt(1 - alpha / (2 * m), nu),
              Scheffe = sqrt((a - 1) * qf(1 - alpha, a - 1, nu)))
print(round(crit[a == 4, ], 3))
matplot(a, crit, type = "b", pch = 19, lty = 1, lwd = 2,
        col = c("steelblue", "darkorange", "forestgreen", "firebrick"),
        xlab = "number of levels a", ylab = "critical value for |t0|",
        main = "Pairwise comparisons, alpha = 0.05, 16 error degrees of freedom")
abline(v = 4, lty = 3, col = "gray")
legend("topleft", bty = "n", lwd = 2, col = c("steelblue", "darkorange", "forestgreen", "firebrick"),
       legend = colnames(crit))
