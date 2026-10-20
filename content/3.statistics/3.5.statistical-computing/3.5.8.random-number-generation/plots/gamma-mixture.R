# Sampling from a mixture of five gamma distributions Gamma(3, rate 1/i) with weights i/15.
set.seed(0)
n <- 5000
k <- sample(1:5, size = n, replace = TRUE, prob = (1:5) / 15)
rate <- 1 / k
x <- rgamma(n, shape = 3, rate = rate)

hist(x, breaks = 80, freq = FALSE, xlim = c(0, 40), col = "lightsteelblue", border = "white",
     main = "Mixture of Gamma(3, 1/i), weights i/15", xlab = "x")
for (i in 1:5) curve(dgamma(x, 3, 1 / i), add = TRUE, lty = 2, col = "gray40")
curve(rowSums(sapply(1:5, function(i) i / 15 * dgamma(x, 3, 1 / i))),
      add = TRUE, col = "firebrick", lwd = 2.5)
lines(density(x), col = "steelblue", lwd = 1.5)   # kernel density estimate of the sample
