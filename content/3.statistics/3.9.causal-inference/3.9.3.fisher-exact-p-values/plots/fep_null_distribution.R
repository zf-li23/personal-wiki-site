# Exact null distribution for six units and a simulated randomization distribution for 72 units.
set.seed(0)
par(mfrow = c(1, 2))

# Left: six honey units, all 20 assignments under the sharp null
y <- c(3, 5, 0, 4, 0, 1)
t_obs <- abs(mean(y[1:3]) - mean(y[4:6]))
tr <- combn(6, 3)
vals <- round(apply(tr, 2, function(i) abs(mean(y[i]) - mean(y[-i]))), 6)
tab <- table(vals)
barplot(tab, names.arg = c("1/3", "1", "5/3", "7/3", "11/3"),
        col = ifelse(as.numeric(names(tab)) >= t_obs - 1e-9, "firebrick", "steelblue"),
        xlab = "absolute difference in means", ylab = "number of assignments (of 20)",
        main = sprintf("Six units: exact p = %.2f", mean(vals >= t_obs - 1e-9)))

# Right: simulated 72-unit experiment with outcomes on a 0-6 scale
n <- 72; n_t <- 35
y0 <- rbinom(n, 6, 0.45)
y1 <- pmin(pmax(y0 - rbinom(n, 1, 0.7), 0), 6)
w_obs <- seq_len(n) %in% sample(n, n_t)
y_obs <- ifelse(w_obs, y1, y0)
d_obs <- mean(y_obs[w_obs]) - mean(y_obs[!w_obs])
diffs <- replicate(1e5, {
  w <- seq_len(n) %in% sample(n, n_t)
  mean(y_obs[w]) - mean(y_obs[!w])
})
p_sim <- mean(abs(diffs) >= abs(d_obs) - 1e-12)
sd_null <- sqrt(n / (n_t * (n - n_t)) * var(y_obs))
hist(diffs, breaks = 45, freq = FALSE, col = "lightsteelblue", border = "white",
     xlab = "difference in means (treated minus control)",
     main = sprintf("72 units (simulated): p = %.3f", p_sim))
curve(dnorm(x, 0, sd_null), add = TRUE, col = "darkorange", lwd = 2)
abline(v = c(d_obs, -d_obs), lty = c(2, 3))
