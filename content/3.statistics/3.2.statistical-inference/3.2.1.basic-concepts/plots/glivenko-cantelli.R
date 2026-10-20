# Kolmogorov distance D_n between the EDF and the true CDF as n grows (20 replications).
set.seed(0)

ks_distance <- function(sample) {
  x <- sort(sample)
  n <- length(x)
  f <- pnorm(x)
  i <- seq_len(n)
  max(pmax(i / n - f, f - (i - 1) / n))
}

ns <- unique(as.integer(10^seq(1, 4, length.out = 25)))
# each column: one sample path of D_n along the growing sample
D <- replicate(20, {
  data <- rnorm(max(ns))
  sapply(ns, function(n) ks_distance(data[1:n]))
})

matplot(ns, D, type = "l", lty = 1, lwd = 0.9, col = adjustcolor("steelblue", 0.35),
        log = "xy", ylim = range(D, 1 / sqrt(ns)),
        xlab = "sample size n", ylab = "D_n = sup |F_n(x) - F(x)|",
        main = "Glivenko-Cantelli: D_n -> 0 almost surely")
lines(ns, 1 / sqrt(ns), col = "firebrick", lwd = 1.6, lty = 2)
legend("topright", bty = "n", legend = "reference 1/sqrt(n)", col = "firebrick", lwd = 1.6, lty = 2)
