# Equal-tailed versus highest posterior density 90% credible intervals for a Beta(3, 12) posterior.
a <- 3
b <- 12
level <- 0.90
eq <- qbeta(c((1 - level) / 2, (1 + level) / 2), a, b)

# HPD: shortest interval [lo, hi] with posterior mass `level`
width <- function(lo) qbeta(pbeta(lo, a, b) + level, a, b) - lo
lo_hpd <- optimize(width, interval = c(0, qbeta(1 - level, a, b) - 1e-9))$minimum
hpd <- c(lo_hpd, qbeta(pbeta(lo_hpd, a, b) + level, a, b))

th <- seq(0, 0.7, length.out = 600)
intervals <- list("Equal-tailed" = eq, "HPD" = hpd)
cols <- c("steelblue", "darkorange")
op <- par(mfrow = c(1, 2))
for (k in 1:2) {
  iv <- intervals[[k]]
  plot(th, dbeta(th, a, b), type = "l", lwd = 1.6, col = "grey30",
       xlab = "theta", ylab = if (k == 1) "posterior density" else "",
       main = sprintf("%s: [%.3f, %.3f], length %.3f", names(intervals)[k], iv[1], iv[2],
                      iv[2] - iv[1]))
  inside <- th >= iv[1] & th <= iv[2]
  polygon(c(iv[1], th[inside], iv[2]), c(0, dbeta(th[inside], a, b), 0),
          col = adjustcolor(cols[k], 0.35), border = NA)
  segments(iv, 0, iv, dbeta(iv, a, b), col = cols[k], lwd = 1.4)
}
abline(h = dbeta(hpd[1], a, b), lty = 3, col = cols[2])   # equal density at both HPD endpoints
par(op)
