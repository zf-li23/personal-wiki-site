# Poisson thinning: N ~ Poi(10) eggs, each hatches with probability 0.3; the number hatched W is Poi(3).
set.seed(0)
lam <- 10
p <- 0.3
reps <- 20000
n <- rpois(reps, lam)
w <- rbinom(reps, size = n, prob = p)

k <- 0:12
freq <- sapply(k, function(j) mean(w == j))
pmf <- dpois(k, lam * p)

bp <- barplot(freq, names.arg = k, col = adjustcolor("steelblue", 0.6), border = NA,
              ylim = c(0, 1.15 * max(freq, pmf)), xlab = "k", ylab = "P(W = k)",
              main = "Random sum of Bernoulli(0.3) over N ~ Poi(10) terms")
lines(bp, pmf, type = "o", pch = 19, lwd = 1.5, col = "firebrick")
legend("topright", bty = "n", pch = c(15, 19), lty = c(NA, 1),
       col = c(adjustcolor("steelblue", 0.6), "firebrick"),
       legend = c("simulated W (20000 runs)", "Poi(lambda p) = Poi(3)"))
