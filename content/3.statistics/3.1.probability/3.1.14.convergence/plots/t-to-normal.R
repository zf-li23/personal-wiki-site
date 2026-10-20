# Densities of t_n for n = 1, 3, 10, 30 converge to the N(0,1) density.
x <- seq(-5, 5, length.out = 800)
ns <- c(1, 3, 10, 30)
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")

plot(x, dnorm(x), type = "l", lwd = 2, lty = 2, xlab = "x", ylab = "density",
     main = "t_n -> N(0, 1) in distribution (Slutsky)")
for (j in seq_along(ns)) lines(x, dt(x, df = ns[j]), col = cols[j], lwd = 1.5)
legend("topright", bty = "n", lty = c(rep(1, 4), 2), col = c(cols, "black"),
       legend = c(paste0("t_", ns), "N(0, 1)"))
