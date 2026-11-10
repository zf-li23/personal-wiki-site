# Randomization distributions of the estimated average effect under CRE, SRE and PRE.
set.seed(0)
n <- 80; reps <- 5000
x <- sort(rnorm(n))
y0 <- 2 * x + rnorm(n)
y1 <- y0 + 1 + 0.5 * rnorm(n)
estimate <- function(w) mean(y1[w]) - mean(y0[!w])

cre <- function() seq_len(n) %in% sample(n, n / 2)
sre <- function(J = 4) {
  size <- n / J
  unlist(lapply(seq_len(J), function(j) seq_len(size) %in% sample(size, size / 2)))
}
pre <- function() {
  first <- runif(n / 2) < 0.5
  as.vector(rbind(first, !first))       # pairs (1, 2), (3, 4), ...
}

est <- sapply(list(CRE = cre, SRE = sre, PRE = pre),
              function(f) replicate(reps, estimate(f())))
print(apply(est, 2, sd))
plot(density(est[, "CRE"]), lwd = 2, col = "steelblue", ylim = c(0, 4),
     main = "Same population, three designs", xlab = "estimated average effect")
lines(density(est[, "SRE"]), lwd = 2, col = "darkorange")
lines(density(est[, "PRE"]), lwd = 2, col = "forestgreen")
abline(v = mean(y1 - y0), lty = 3)
