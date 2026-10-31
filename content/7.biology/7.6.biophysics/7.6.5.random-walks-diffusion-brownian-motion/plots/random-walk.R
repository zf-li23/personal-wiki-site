# Random walks in two dimensions: unit steps in random directions; ensemble MSD and the
# distribution of x after N steps compared with the Gaussian limit.
set.seed(1)
M <- 2000; N <- 1000
theta <- matrix(runif(M * N, 0, 2 * pi), M, N)
x <- t(apply(cos(theta), 1, cumsum))
y <- t(apply(sin(theta), 1, cumsum))

# ensemble mean squared displacement against number of steps
msd <- colMeans(x^2 + y^2)
n <- 1:N
plot(n, msd, log = "xy", pch = 16, cex = 0.4, xlab = "steps N", ylab = "<r^2> / a^2")
abline(0, 1, col = "red")   # <r^2> = N a^2 = 4 D t
fit <- lm(msd ~ 0 + n)
print(coef(fit))            # slope close to 1

# distribution of x after 400 steps against the Gaussian of variance N a^2 / 2
hist(x[, 400] / sqrt(400), breaks = 40, freq = FALSE, xlab = "x / (sqrt(N) a)", main = "")
curve(dnorm(x, sd = sqrt(0.5)), add = TRUE, col = "red")
