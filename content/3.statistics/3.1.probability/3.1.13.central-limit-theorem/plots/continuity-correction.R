# Bin(36, 0.5) pmf with the N(18, 9) density; the area over [k - 0.5, k + 0.5] approximates P(S_n = k).
n <- 36
p <- 0.5
mu <- n * p
sigma <- sqrt(n * p * (1 - p))
k <- 6:30
x <- seq(5, 31, length.out = 600)

exact <- pbinom(21, n, p)
corrected <- pnorm(21.5, mu, sigma)
plot(k, dbinom(k, n, p), type = "h", lwd = 3, col = "steelblue", xlim = c(5, 31),
     ylim = c(0, 1.1 * dbinom(18, n, p)), xlab = "k", ylab = "probability / density",
     main = sprintf("Continuity correction for Bin(36, 0.5): P(S_n <= 21) = %.4f, normal %.4f",
                    exact, corrected), cex.main = 0.9)
xs <- seq(5, 21.5, length.out = 300)
polygon(c(xs, rev(xs)), c(dnorm(xs, mu, sigma), rep(0, length(xs))),
        col = adjustcolor("forestgreen", 0.15), border = NA)
k0 <- 19
xs <- seq(k0 - 0.5, k0 + 0.5, length.out = 50)
polygon(c(xs, rev(xs)), c(dnorm(xs, mu, sigma), rep(0, length(xs))),
        col = adjustcolor("darkorange", 0.5), border = NA)
lines(x, dnorm(x, mu, sigma), col = "firebrick", lwd = 1.5)
abline(v = 21.5, lty = 2, col = "forestgreen")
legend("topright", bty = "n", cex = 0.8, lty = c(1, 1, NA, NA), lwd = c(3, 1.5, NA, NA),
       pch = c(NA, NA, 15, 15),
       col = c("steelblue", "firebrick", adjustcolor("darkorange", 0.5), adjustcolor("forestgreen", 0.3)),
       legend = c("P(S_n = k), exact", "N(18, 9) density", "area for k = 19",
                  "P(S_n <= 21) with correction"))
