# Randomization test for correlation: Monte Carlo null distribution of r.
set.seed(123456)
price <- c(5.0, 4.8, 4.7, 4.0, 5.3, 4.1, 5.5, 4.7, 3.3, 4.0,
           4.0, 4.6, 5.3, 3.0, 3.5, 3.9, 4.7, 5.0, 5.2, 4.6)
quantity <- c(60, 59, 58, 47, 65, 48, 67, 70, 55, 63,
              62, 65, 71, 56, 59, 60, 74, 77, 78, 62)
nrep <- 50000
r_obs <- cor(price, quantity)
r_perm <- replicate(nrep, cor(sample(price), quantity))
p_one <- mean(r_perm >= r_obs)
p_two <- mean(abs(r_perm) >= abs(r_obs))

hist(r_perm, breaks = 60, freq = FALSE, col = "lightblue", border = NA,
     xlab = "sample correlation of permuted prices with quantities",
     main = sprintf("one-sided p = %.4f, two-sided p = %.4f", p_one, p_two))
abline(v = r_obs, col = "red", lwd = 2)
abline(v = -r_obs, col = "red", lty = 2)
