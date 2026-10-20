# Poisson PMFs, the Poisson approximation of Bin(n, lambda/n), and a Poisson fit to the Rutherford-Geiger alpha-particle counts.
op <- par(mfrow = c(1, 3), mar = c(4, 4, 2.5, 1))

k <- 0:15
lams <- 1:6
matplot(k, sapply(lams, function(l) dpois(k, l)), type = "o", lty = 1, pch = 19, cex = 0.5,
        col = 1:6, xlab = "k", ylab = "P(X = k)", main = "Poi(lambda)")
legend("topright", bty = "n", cex = 0.8, lty = 1, col = 1:6, legend = paste("lambda =", lams))

lam <- 3
k <- 0:11
ns <- c(6, 15, 60)
probs <- rbind(t(sapply(ns, function(n) dbinom(k, n, lam / n))), dpois(k, lam))
barplot(probs, beside = TRUE, names.arg = k, border = NA,
        col = c("steelblue", "darkorange", "forestgreen", "firebrick"),
        xlab = "k", main = "Bin(n, lambda/n) approaches Poi(lambda)",
        legend.text = c(paste0("Bin(", ns, ", 3/", ns, ")"), "Poi(3)"),
        args.legend = list(x = "topright", bty = "n", cex = 0.8))

counts <- c(57, 203, 383, 525, 532, 408, 273, 139, 45, 27, 16)
N <- sum(counts)
lam <- 10094 / N                       # total number of particles / number of intervals
k <- 0:10
pois <- dpois(k, lam)
pois[11] <- ppois(9, lam, lower.tail = FALSE)   # last class is "10 or more"
plot(k, counts / N, type = "o", pch = 19, col = "firebrick", xaxt = "n",
     ylim = range(0, counts / N, pois), xlab = "alpha particles per 7.5 s", ylab = "",
     main = "Rutherford-Geiger (1910), N = 2608 intervals")
lines(k, pois, type = "o", pch = 15, lty = 2, col = "steelblue")
axis(1, at = k, labels = c(0:9, "10+"))
legend("topright", bty = "n", cex = 0.8, lty = c(1, 2), pch = c(19, 15),
       col = c("firebrick", "steelblue"),
       legend = c("observed frequency m_k / N", sprintf("Poi(%.2f)", lam)))
par(op)
