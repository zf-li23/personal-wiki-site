# LLN and CLT together for Exp(1) samples: M_n concentrates at 1 (LLN) with an approximately N(1, 1/n) shape (CLT).
set.seed(0)
reps <- 20000
x <- seq(0, 3, length.out = 600)
ns <- c(1, 5, 25, 100)
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")
breaks <- seq(0, 3, length.out = 121)

plot(NA, xlim = c(0, 3), ylim = c(0, 4.3), xlab = "sample mean", ylab = "density",
     main = "Exp(1) sample means (solid) and N(1, 1/n) approximations (dashed)")
for (j in seq_along(ns)) {
  n <- ns[j]
  m <- rowMeans(matrix(rexp(reps * n), nrow = reps))
  h <- hist(m[m <= 3], breaks = breaks, plot = FALSE)
  plot(h, freq = FALSE, add = TRUE, col = NA, border = cols[j])
  if (n > 1) lines(x, dnorm(x, 1, 1 / sqrt(n)), col = cols[j], lty = 2)
}
abline(v = 1)
legend("topright", bty = "n", lty = 1, col = cols, legend = paste0("M_n, n = ", ns))
