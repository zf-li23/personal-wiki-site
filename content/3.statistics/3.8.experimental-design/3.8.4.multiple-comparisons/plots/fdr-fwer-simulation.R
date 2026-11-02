# Simulated FDR, FWER and power of no correction, Benjamini-Hochberg and Bonferroni (1000 tests, 80% true nulls).
set.seed(0)
m <- 1000; m0 <- 800; reps <- 1000; shift <- 2.5; alpha <- 0.05
methods <- c("none", "BH", "bonferroni")
res <- array(NA, dim = c(reps, 3, 3), dimnames = list(NULL, methods, c("FDP", "anyV", "power")))
for (r in 1:reps) {
  z <- rnorm(m); z[(m0 + 1):m] <- z[(m0 + 1):m] + shift
  p <- pnorm(z, lower.tail = FALSE)
  for (k in methods) {
    rej <- p.adjust(p, method = k) <= alpha
    V <- sum(rej[1:m0]); R <- sum(rej)
    res[r, k, ] <- c(V / max(R, 1), V > 0, mean(rej[(m0 + 1):m]))
  }
}
avg <- apply(res, c(2, 3), mean)
print(round(avg, 3))

op <- par(mfrow = c(1, 2))
cols <- c("steelblue", "darkorange", "forestgreen")
br <- seq(0, 0.3, by = 0.005)
hist(res[, "none", "FDP"], breaks = br, col = adjustcolor(cols[1], 0.6), border = NA, ylim = c(0, reps),
     xlab = "false discovery proportion", main = "False discovery proportion")
hist(res[, "BH", "FDP"], breaks = br, col = adjustcolor(cols[2], 0.6), border = NA, add = TRUE)
hist(res[, "bonferroni", "FDP"], breaks = br, col = adjustcolor(cols[3], 0.6), border = NA, add = TRUE)
abline(v = alpha, lty = 2)
legend("topright", fill = cols, legend = c("uncorrected", "BH", "Bonferroni"), bty = "n")
barplot(t(avg), beside = TRUE, col = cols, ylim = c(0, 1.1), main = "Averages over 1000 replications")
abline(h = alpha, lty = 2)
par(op)
