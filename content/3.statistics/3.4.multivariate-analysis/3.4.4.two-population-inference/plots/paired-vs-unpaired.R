# Paired data: overlapping marginal samples, but within-pair differences clearly shifted from zero.
set.seed(0)
n <- 16
size <- rnorm(n, 17.5, 2.0)                  # person-to-person variation
left <- size + rnorm(n, 0, 0.15)
right <- size + 0.25 + rnorm(n, 0, 0.15)     # small systematic shift
diff <- left - right

# The two-sample test ignores the pairing; the paired test works with the differences.
print(t.test(left, right))
print(t.test(left, right, paired = TRUE))

par(mfrow = c(1, 3))
boxplot(list(Left = left, Right = right), ylab = "hand size", main = "marginal samples (unpaired view)")

lim <- range(left, right) + c(-0.5, 0.5)
plot(left, right, pch = 19, col = "steelblue", xlim = lim, ylim = lim, asp = 1,
     xlab = "left", ylab = "right", main = "paired observations")
abline(0, 1, col = "firebrick", lwd = 1.2)

stripchart(diff, method = "jitter", pch = 19, col = "darkorange",
           xlab = "left - right", main = "within-pair differences")
abline(v = 0, col = "firebrick", lwd = 1.2)
