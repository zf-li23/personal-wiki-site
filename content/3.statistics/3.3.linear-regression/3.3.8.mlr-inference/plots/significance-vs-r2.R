# Same mean structure, different noise: a significant slope does not imply a large R^2.
set.seed(0)
n <- 200
x <- runif(n, 0, 200)
ys <- lapply(c(50, 280), function(s) 45 + 2.1 * x + rnorm(n, 0, s))

op <- par(mfrow = c(1, 2), oma = c(0, 0, 2, 0))
for (k in 1:2) {
  y <- ys[[k]]
  fit <- lm(y ~ x)
  s <- summary(fit)
  plot(x, y, pch = 19, cex = 0.6, col = adjustcolor("steelblue", 0.7), ylim = range(unlist(ys)),
       ylab = if (k == 1) "y" else "",
       main = sprintf("slope p-value = %.1e,  R^2 = %.2f", coef(s)["x", "Pr(>|t|)"], s$r.squared))
  abline(fit, col = "firebrick", lwd = 2)
}
mtext("Both slopes are highly significant; only the scatter around the line differs", outer = TRUE)
par(op)
