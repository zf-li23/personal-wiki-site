# Lattice structure of linear congruential generators: successive pairs for m = 101 with
# a = 3 and a = 12, and RANDU triples projected on the normal (9, -6, 1) of its planes.
lcg <- function(a, c, m, x0, n) {
  x <- numeric(n)
  for (i in 1:n) {
    x0 <- (a * x0 + c) %% m   # exact in double precision for these moduli
    x[i] <- x0
  }
  x / m
}

par(mfrow = c(1, 3))
for (a in c(3, 12)) {
  r <- lcg(a, 0, 101, 1, 100)
  plot(r[-100], r[-1], pch = 20, asp = 1, xlab = "R_i", ylab = "R_(i+1)",
       main = sprintf("LCG m = 101, a = %d", a))
}

n <- 3000
r <- lcg(65539, 0, 2^31, 1, n + 2)          # RANDU
u <- runif(n + 2)                           # R's default Mersenne Twister
proj <- function(v) 9 * v[1:n] - 6 * v[2:(n + 1)] + v[3:(n + 2)]
plot(proj(u), u[3:(n + 2)], pch = ".", col = "gray50",
     xlab = "9 R_i - 6 R_(i+1) + R_(i+2)", ylab = "R_(i+2)", main = "RANDU vs Mersenne Twister")
points(proj(r), r[3:(n + 2)], pch = ".", col = "firebrick")
table(round(proj(r)))                       # only the 15 integers -5, ..., 9 occur
