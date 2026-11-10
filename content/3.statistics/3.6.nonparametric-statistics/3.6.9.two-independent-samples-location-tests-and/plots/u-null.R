# Exact null distribution of the Mann-Whitney U for n1 = 10, n2 = 11, with the normal approximation.
A <- c(23, 18, 17, 25, 22, 19, 31, 26, 29, 33)
B <- c(21, 28, 32, 30, 41, 24, 35, 34, 27, 39, 36)
n1 <- length(A); n2 <- length(B)
print(wilcox.test(A, B))                       # W = 21, p-value = 0.01587
u <- 0:(n1 * n2)
p <- dwilcox(u, n1, n2)
crit <- qwilcox(0.025, n1, n2) - 1             # 26
print(c(crit = crit, size = 2 * pwilcox(crit, n1, n2)))
barplot(p, names.arg = u, space = 0, col = ifelse(u <= crit | u >= n1 * n2 - crit, "firebrick", "steelblue"),
        xlab = "U", ylab = "probability", main = "WMW test, n1 = 10, n2 = 11")
curve(dnorm(x, n1 * n2 / 2, sqrt(n1 * n2 * (n1 + n2 + 1) / 12)), add = TRUE, lwd = 2, col = "darkorange",
      from = 0, to = n1 * n2)
