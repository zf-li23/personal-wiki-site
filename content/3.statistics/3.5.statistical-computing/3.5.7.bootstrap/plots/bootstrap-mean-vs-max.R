# Bootstrap distributions of the sample mean and the sample maximum for one sample of size
# n = 50 from U(0, 1).
set.seed(0)
n <- 50; B <- 2000
x <- runif(n)
means <- maxima <- numeric(B)
for (b in 1:B) {
  xb <- sample(x, n, replace = TRUE)
  means[b] <- mean(xb)
  maxima[b] <- max(xb)
}
mean(maxima == max(x))   # close to 1 - (1 - 1/n)^n, about 0.64

par(mfrow = c(1, 2))
hist(means, breaks = 40, freq = FALSE, col = "lightsteelblue", border = "white",
     main = "Sample mean", xlab = "bootstrap mean")
abline(v = mean(x), col = "firebrick", lwd = 2)
tab <- table(maxima) / B
plot(as.numeric(names(tab)), as.numeric(tab), type = "h", lwd = 3, col = "darkorange",
     xlab = "bootstrap maximum", ylab = "relative frequency", main = "Sample maximum")
abline(v = max(x), col = "firebrick", lty = 2)
