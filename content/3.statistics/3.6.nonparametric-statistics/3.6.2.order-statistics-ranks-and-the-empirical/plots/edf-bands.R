# EDF with pointwise Clopper-Pearson intervals and the DKW confidence band.
set.seed(3)
n <- 50; x <- sort(rnorm(n)); Fn <- ecdf(x)
l1 <- u1 <- l2 <- u2 <- numeric(n)
epsilon <- sqrt(log(2 / 0.05) / (2 * n))
for (i in 1:n) {
  ci <- binom.test(sum(x <= x[i]), n)$conf.int   # Clopper-Pearson interval for F(x_i)
  l1[i] <- ci[1]; u1[i] <- ci[2]
  l2[i] <- max(Fn(x[i]) - epsilon, 0); u2[i] <- min(Fn(x[i]) + epsilon, 1)
}
plot(Fn, verticals = TRUE, do.points = FALSE, xlab = "x", ylab = "F_n(x)",
     main = "Confidence intervals and band")
polygon(c(x, rev(x)), c(l2, rev(u2)), col = "gray85", border = FALSE)
polygon(c(x, rev(x)), c(l1, rev(u1)), col = "gray70", border = FALSE)
plot(Fn, verticals = TRUE, do.points = FALSE, add = TRUE)
curve(pnorm(x), add = TRUE, col = "red")
