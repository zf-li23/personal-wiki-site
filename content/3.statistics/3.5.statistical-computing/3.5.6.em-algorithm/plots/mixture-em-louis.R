# Two-part normal mixture: EM for the mixing proportion and Louis's acceleration.
mu1 <- 1; s1 <- 2; mu2 <- 4; s2 <- 1; a0 <- 0.4; n <- 100
set.seed(5288)
z <- rbinom(n, 1, a0)
x <- rnorm(n, mu1 * z + mu2 * (1 - z), s1 * z + (1 - z) * s2)
f1 <- dnorm(x, mu1, s1); f2 <- dnorm(x, mu2, s2)

loglik <- function(a) sum(log(a * f1 + (1 - a) * f2))
Lambda <- function(a) a * f1 / (a * f1 + (1 - a) * f2)       # responsibilities
M <- function(a) mean(Lambda(a))                              # one EM step
Ix <- function(a) sum(((f1 - f2) / (a * f1 + (1 - a) * f2))^2)  # observed information
Ic <- function(a) { lam <- Lambda(a); sum(lam / a^2 + (1 - lam) / (1 - a)^2) }  # complete
Mstar <- function(a) a + Ic(a) / Ix(a) * (M(a) - a)           # Louis-accelerated step

mle <- 0.5
for (i in 1:100) {  # Newton on the score, for a reference value of the MLE
  lam <- Lambda(mle)
  mle <- mle + sum(lam / mle - (1 - lam) / (1 - mle)) / Ix(mle)
}
iter <- 8
EM <- Accel <- numeric(iter)
a <- astar <- 0.1
for (i in 1:iter) {
  a <- M(a); astar <- Mstar(astar)
  EM[i] <- a; Accel[i] <- astar
}
results <- data.frame(EM = EM, Accel = Accel, errorEM = abs(EM - mle), errorAccel = abs(Accel - mle))
print(format(results, scientific = FALSE))

op <- par(mfrow = c(1, 2))
hist(x, breaks = 14, freq = FALSE, col = "lightblue", main = sprintf("alpha_hat = %.4f", mle))
rug(x)
curve(mle * dnorm(x, mu1, s1) + (1 - mle) * dnorm(x, mu2, s2), add = TRUE, col = "firebrick", lwd = 2)
plot(0:iter, abs(c(0.1, EM) - mle), log = "y", type = "b", pch = 19, col = "steelblue",
     xlab = "iteration", ylab = "|alpha_t - MLE|", main = "start alpha_0 = 0.1",
     ylim = c(1e-15, 1))
lines(0:iter, pmax(abs(c(0.1, Accel) - mle), 1e-15), type = "b", pch = 15, col = "firebrick")
legend("bottomleft", bty = "n", legend = c("standard EM", "Louis acceleration"),
       col = c("steelblue", "firebrick"), pch = c(19, 15))
par(op)
