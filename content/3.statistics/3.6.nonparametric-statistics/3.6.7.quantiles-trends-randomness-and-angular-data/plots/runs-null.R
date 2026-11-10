# Exact null distribution of the number of runs for m = n = 10, with the normal approximation.
runs_pmf <- function(m, n) {
  r <- 2:(m + n)
  p <- sapply(r, function(rr) {
    s <- rr %/% 2
    if (rr %% 2 == 0) 2 * choose(m - 1, s - 1) * choose(n - 1, s - 1)
    else choose(m - 1, s - 1) * choose(n - 1, s) + choose(m - 1, s) * choose(n - 1, s - 1)
  })
  data.frame(r = r, p = p / choose(m + n, m))
}
runs_test <- function(seq) {
  s <- strsplit(seq, "")[[1]]
  R <- 1 + sum(s[-1] != s[-length(s)])
  m <- sum(s == s[1]); n <- length(s) - m; N <- m + n
  d <- runs_pmf(m, n)
  exact <- min(1, 2 * min(sum(d$p[d$r <= R]), sum(d$p[d$r >= R])))
  mu <- 1 + 2 * m * n / N
  v <- 2 * m * n * (2 * m * n - N) / (N^2 * (N - 1))
  z <- (R - mu + ifelse(R < mu, 0.5, -0.5)) / sqrt(v)
  c(R = R, exact = exact, asymptotic = 2 * pnorm(-abs(z)))
}
for (s in c("HHHHHTTTTTTTTTTHHHHH", "HTHTHTHTHTHTHTHTHTHT", "HHTHTTTHTHHTHTHHHTTH"))
  print(round(runs_test(s), 5))

d <- runs_pmf(10, 10)
barplot(d$p, names.arg = d$r, col = ifelse(d$r <= 6 | d$r >= 16, "firebrick", "steelblue"),
        xlab = "number of runs R", ylab = "probability", main = "Runs test, m = n = 10")
