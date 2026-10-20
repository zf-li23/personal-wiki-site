# Sample paths of the running mean of fair-coin tosses, with the band p +- 0.03.
set.seed(0)
p <- 0.5
eps <- 0.03
n_max <- 2000
paths <- 20
n <- 1:n_max
x <- matrix(rbinom(paths * n_max, 1, p), nrow = n_max)   # one column per path
means <- apply(x, 2, cumsum) / n

matplot(n, means, type = "l", lty = 1, lwd = 0.8, log = "x", ylim = c(0, 1),
        col = adjustcolor(hcl.colors(paths, "Dark 3"), 0.7),
        xlab = "n (log scale)", ylab = "M_n = (X_1 + ... + X_n) / n",
        main = "Running means of Ber(0.5): 20 sample paths and the band 0.5 +- 0.03")
abline(h = p, lwd = 1.2)
abline(h = c(p - eps, p + eps), lty = 2)
