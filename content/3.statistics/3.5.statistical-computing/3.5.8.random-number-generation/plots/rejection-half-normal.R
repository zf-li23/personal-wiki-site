# Envelope rejection sampling of the half-normal density with Exp(1) proposals,
# followed by a random sign to obtain standard normal variates.
set.seed(0)
lambda <- 1
cc <- sqrt(2 / pi) / lambda * exp(lambda^2 / 2)   # smallest c with f <= c g

n <- 4000
x <- rexp(n, rate = lambda)
u <- runif(n)
accept <- u <= exp(-(x - lambda)^2 / 2)            # u <= f(x) / (c g(x))
mean(accept)                                       # close to 1 / cc = 0.760

par(mfrow = c(1, 2))
h <- cc * dexp(x, lambda) * u
plot(x[1:1200], h[1:1200], pch = 20, cex = 0.4,
     col = ifelse(accept[1:1200], "steelblue", "firebrick"),
     xlim = c(0, 4.5), ylim = c(0, 1.4), xlab = "x", ylab = "",
     main = "Accepted (blue) and rejected (red)")
curve(cc * dexp(x, lambda), add = TRUE, col = "darkorange", lwd = 2)
curve(2 * dnorm(x), add = TRUE, col = "steelblue", lwd = 2)

z <- sample(c(-1, 1), sum(accept), replace = TRUE) * x[accept]
hist(z, breaks = 40, freq = FALSE, col = "lightsteelblue", border = "white",
     main = "Resulting N(0, 1) sample", xlab = "z")
curve(dnorm(x), add = TRUE, col = "firebrick", lwd = 2)
