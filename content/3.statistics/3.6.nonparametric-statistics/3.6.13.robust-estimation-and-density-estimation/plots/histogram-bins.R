# The same 40 observations in four histograms: two bin widths and two bin origins.
x <- c(6.1, 4.7, 4.1, 4.6, 6.0, 5.5, 4.6, 5.8, 5.6, 5.0,
       5.9, 4.9, 3.9, 4.9, 4.0, 3.1, 4.9, 6.1, 3.1, 4.3,
       4.9, 6.0, 1.4, 3.9, 6.1, 5.3, 2.7, 6.9, 5.2, 3.8,
       8.2, 8.5, 8.1, 4.9, 8.4, 8.4, 7.3, 3.4, 10.7, 4.7)
settings <- list(c(2, 0), c(2, 1), c(0.5, 0), c(0.5, 0.25))
op <- par(mfrow = c(2, 2), mar = c(4, 4, 2, 1))
for (s in settings) {
  breaks <- seq(s[2] - s[1], 12 + s[1], by = s[1])
  hist(x, breaks = breaks, freq = FALSE, xlim = c(0, 12), col = "lightblue",
       main = sprintf("bin width %g, origin %g", s[1], s[2]), xlab = "x")
  rug(x)
}
par(op)
