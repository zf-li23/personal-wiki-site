# Matching problem: probability of no match q0(n), and the number of matches for n = 10 (exact, Poisson limit, simulation).
q <- function(r, n) {
  k <- 0:(n - r)
  sum((-1)^k / factorial(k)) / factorial(r)
}

op <- par(mfrow = c(1, 2), mar = c(4, 4, 2.5, 1))
ns <- 1:12
q0 <- sapply(ns, function(n) q(0, n))
plot(ns, q0, type = "o", pch = 19, col = "steelblue", ylim = c(-0.05, 0.6), xaxt = "n",
     xlab = "number of letters n", ylab = "P(no letter in the correct envelope)",
     main = "No match: rapid convergence to 1/e")
axis(1, at = ns)
abline(h = exp(-1), lty = 2, lwd = 1.2, col = "firebrick")
legend("topright", bty = "n", cex = 0.8, lty = c(1, 2), pch = c(19, NA),
       col = c("steelblue", "firebrick"),
       legend = c("q0(n) = sum_{k=0}^{n} (-1)^k / k!", "1/e = 0.3679"))

set.seed(0)
n <- 10
rs <- 0:6
exact <- sapply(rs, function(r) q(r, n))
poisson <- dpois(rs, 1)
sims <- replicate(20000, sum(sample(n) == 1:n))
freq <- sapply(rs, function(r) mean(sims == r))
barplot(rbind(exact, poisson, freq), beside = TRUE, names.arg = rs,
        col = c("steelblue", "darkorange", "forestgreen"), border = NA,
        xlab = "number of correct letters r", ylab = "probability",
        main = paste("Number of matches, n =", n),
        legend.text = c(paste0("exact q_r(", n, ")"), "limit e^{-1} / r!", "20000 random permutations"),
        args.legend = list(x = "topright", bty = "n", cex = 0.8))
par(op)
