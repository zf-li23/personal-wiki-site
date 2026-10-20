# Power of the slope t-test as an area under a noncentral t density (Toluca planning example).
df <- 23
delta <- 1.5 / sqrt(2500 / 19800)
cval <- qt(0.975, df)
power <- pt(cval, df, ncp = delta, lower.tail = FALSE) + pt(-cval, df, ncp = delta)

shade <- function(x, f, keep, col) {
  # fill the area under f over the contiguous region where keep is TRUE
  xs <- x[keep]; fs <- f[keep]
  polygon(c(xs[1], xs, xs[length(xs)]), c(0, fs, 0), col = col, border = NA)
}

op <- par(mfrow = c(1, 2))
x <- seq(-5, 10, length.out = 600)
f0 <- dt(x, df)
f1 <- dt(x, df, ncp = delta)
plot(x, f0, type = "l", lwd = 2, col = "steelblue", ylim = c(0, 0.58),
     xlab = "t", ylab = "density", main = sprintf("Critical values +/- %.3f", cval))
lines(x, f1, lwd = 2, col = "firebrick")
shade(x, f1, x > cval, adjustcolor("firebrick", 0.3))
shade(x, f1, x < -cval, adjustcolor("firebrick", 0.3))
shade(x, f0, x > cval, adjustcolor("steelblue", 0.3))
shade(x, f0, x < -cval, adjustcolor("steelblue", 0.3))
abline(v = c(-cval, cval), lty = 2, col = "gray")
legend("topright", bty = "n", cex = 0.75, lwd = c(2, 2, 8, 8),
       col = c("steelblue", "firebrick", adjustcolor("firebrick", 0.3), adjustcolor("steelblue", 0.3)),
       legend = c("t_23 (under H0: beta_1 = 0)",
                  sprintf("t_23(delta = %.2f) (beta_1 = 1.5)", delta),
                  sprintf("power = %.3f", power), "alpha = 0.05"))

x <- seq(-5, 6, length.out = 500)
settings <- list(c(0, 1), c(0, 4), c(2, 1), c(2, 4))   # (delta, df)
dens <- sapply(settings, function(s) if (s[1] == 0) dt(x, s[2]) else dt(x, s[2], ncp = s[1]))
cols <- c("steelblue", "darkorange", "forestgreen", "firebrick")
matplot(x, dens, type = "l", lty = 1, lwd = 1.8, col = cols,
        xlab = "t", ylab = "density", main = "Noncentral t densities")
legend("topleft", bty = "n", cex = 0.75, lwd = 1.8, col = cols,
       legend = sapply(settings, function(s) sprintf("delta = %g, df = %g", s[1], s[2])))
par(op)
