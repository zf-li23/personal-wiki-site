# Binomial partitioning at division and the calibration of single-molecule brightness from the
# daughter-to-daughter differences, <(I1 - I2)^2> = alpha (I1 + I2).
set.seed(11)

# A: fraction received by one daughter for N = 10, 100, 1000
par(mfrow = c(1, 2))
f <- rbinom(20000, 1000, 0.5) / 1000
hist(f, breaks = 60, freq = FALSE, xlab = "n1 / N", main = "N = 1000")
curve(dnorm(x, 0.5, 0.5 / sqrt(1000)), add = TRUE, col = "red")
for (N in c(10, 100, 1000)) cat(N, sd(rbinom(20000, N, 0.5) / N), 0.5 / sqrt(N), "\n")

# B: simulated calibration experiment
alpha <- 50
N <- as.integer(exp(runif(400, log(20), log(2000))))
n1 <- rbinom(length(N), N, 0.5)
I1 <- alpha * n1 * (1 + 0.005 * rnorm(length(N)))
I2 <- alpha * (N - n1) * (1 + 0.005 * rnorm(length(N)))
It <- I1 + I2; dI2 <- (I1 - I2)^2
plot(It, dI2, log = "xy", pch = 16, cex = 0.4, xlab = "I1 + I2", ylab = "(I1 - I2)^2")
alpha_hat <- mean(dI2 / It)
abline(log10(alpha_hat), 1, col = "red")   # straight line of slope 1 on log axes
print(alpha_hat)                            # close to the true value 50
print(coef(lm(dI2 ~ 0 + It)))              # least squares, dominated by the brightest cells
