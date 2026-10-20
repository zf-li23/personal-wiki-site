# A continuous X and a group indicator: Simpson's paradox, parallel lines, interaction.
set.seed(0)
op <- par(mfrow = c(1, 3))

# Simpson's paradox: positive slope within groups, negative pooled slope
centers <- list(c(2.5, 7.5), c(9.5, 2.5))
cols <- c("steelblue", "firebrick")
xs <- ys <- list()
for (k in 1:2) {
  cx <- centers[[k]][1]; cy <- centers[[k]][2]
  xs[[k]] <- cx + runif(25, -2, 2)
  ys[[k]] <- cy + 1.0 * (xs[[k]] - cx) + rnorm(25, 0, 0.6)
}
x <- unlist(xs); y <- unlist(ys); grp <- rep(1:2, each = 25)
plot(x, y, pch = 19, col = cols[grp], xlim = c(0, 12), xlab = "X1", ylab = "Y", main = "Simpson's paradox")
for (k in 1:2) {
  fk <- lm(ys[[k]] ~ xs[[k]])
  r <- range(xs[[k]])
  lines(r, coef(fk)[1] + coef(fk)[2] * r, col = cols[k], lwd = 2)
}
abline(lm(y ~ x), col = "gray20", lty = 2, lwd = 2)
legend("topright", bty = "n", cex = 0.8, pch = c(19, 19, NA), lty = c(NA, NA, 2),
       col = c(cols, "gray20"), legend = c("group 1", "group 2", "pooled"))

# additive versus interaction: fit Y ~ X1 * X2 and test the interaction term
x <- runif(40, 0, 10)
g <- sample(0:1, 40, replace = TRUE)
for (case in list(list(slopes = c(1, 1), title = "Additive: parallel lines"),
                  list(slopes = c(1, 0.3), title = "Interaction: different slopes"))) {
  y <- 2 + 3 * g + ifelse(g == 0, case$slopes[1], case$slopes[2]) * x + rnorm(40, 0, 0.8)
  fit <- lm(y ~ x * g)
  b <- coef(fit)   # (Intercept), x, g, x:g
  p_int <- coef(summary(fit))["x:g", "Pr(>|t|)"]
  plot(x, y, pch = 19, col = cols[g + 1], xlab = "X1", ylab = "",
       main = sprintf("%s\ninteraction p-value = %.3g", case$title, p_int), cex.main = 0.9)
  abline(a = b[1], b = b[2], col = cols[1], lwd = 2)
  abline(a = b[1] + b[3], b = b[2] + b[4], col = cols[2], lwd = 2)
  legend("topleft", bty = "n", cex = 0.8, pch = 19, col = cols, legend = c("X2 = 0", "X2 = 1"))
}
par(op)
