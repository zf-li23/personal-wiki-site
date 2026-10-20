# Birthday problem: probability that among n people at least two share a birthday (365 days), exact and approximate.
N <- 365
n <- 1:80
p_share <- 1 - cumprod((N - n + 1) / N)    # the same values as pbirthday(n) in base R
approx <- 1 - exp(-n * (n - 1) / (2 * N))
n50 <- which(p_share >= 0.5)[1]

plot(n, p_share, type = "l", lwd = 2, col = "steelblue", xlim = c(0, 80), ylim = c(0, 1.02),
     xlab = "number of people n", ylab = "P(at least two share a birthday)",
     main = sprintf("n = %d: %.3f", n50, p_share[n50]))
lines(n, approx, lwd = 1.5, lty = 2, col = "darkorange")
abline(h = 0.5, v = n50, lty = 3, col = "gray")
legend("bottomright", bty = "n", cex = 0.85, lty = c(1, 2), lwd = c(2, 1.5),
       col = c("steelblue", "darkorange"),
       legend = c("exact: 1 - N!/((N-n)! N^n)", "approx: 1 - exp(-n(n-1)/(2N))"))
