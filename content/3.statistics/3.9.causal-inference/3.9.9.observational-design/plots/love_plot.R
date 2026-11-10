# Love plot: absolute normalized differences before and after matching (simulated data).
set.seed(0)
n_t <- 300; n_c <- 1500
draw <- function(n, shift) {
  z <- matrix(rnorm(3 * n), n)
  cbind(age = 35 + 8 * (z[, 1] + shift),
        education = 12 + 2 * (0.5 * z[, 1] + z[, 2] + 0.6 * shift),
        earnings = 20 + 6 * (z[, 3] - 0.8 * shift),
        married = as.numeric(runif(n) < 0.5 + 0.15 * shift),
        children = rpois(n, 1.2 + 0.4 * shift),
        region = as.numeric(runif(n) < 0.4))
}
x_t <- draw(n_t, 0.6); x_c <- draw(n_c, 0)
x <- rbind(x_t, x_c); w <- rep(1:0, c(n_t, n_c))

norm_diff <- function(a, b)
  abs(colMeans(a) - colMeans(b)) / sqrt((apply(a, 2, var) + apply(b, 2, var)) / 2)

lin <- predict(glm(w ~ scale(x), family = binomial))   # linearized propensity score
s_inv <- solve(cov(x_c))

match <- function(dist) {          # greedy 1:1 nearest neighbour without replacement
  free <- rep(TRUE, n_c); chosen <- integer(n_t)
  for (i in seq_len(n_t)) {
    d <- dist(i); d[!free] <- Inf
    chosen[i] <- which.min(d); free[chosen[i]] <- FALSE
  }
  x_c[chosen, ]
}
d_mahal <- function(i) mahalanobis(x_c, x_t[i, ], s_inv, inverted = TRUE)
d_ps <- function(i) abs(lin[(n_t + 1):(n_t + n_c)] - lin[i])

res <- rbind(before = norm_diff(x_t, x_c),
             mahalanobis = norm_diff(x_t, match(d_mahal)),
             pscore = norm_diff(x_t, match(d_ps)))
dotchart(t(res)[ncol(res):1, 1], pch = 19, col = "firebrick",
         xlim = c(0, max(res)), xlab = "absolute normalized difference")
points(rev(res[2, ]), seq_len(ncol(res)), pch = 15, col = "steelblue")
points(rev(res[3, ]), seq_len(ncol(res)), pch = 17, col = "darkgreen")
abline(v = 0.1, lty = 2)
legend("bottomright", rownames(res), pch = c(19, 15, 17),
       col = c("firebrick", "steelblue", "darkgreen"), bty = "n")
