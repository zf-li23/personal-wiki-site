# PC algorithm with Fisher-z tests on simulated linear Gaussian data: structure recovery versus sample size
library(bnlearn)
set.seed(0)
nodes <- paste0("X", 1:5)
true_dag <- empty.graph(nodes)
arcs(true_dag) <- matrix(c("X1", "X2", "X1", "X3", "X2", "X4", "X3", "X4", "X3", "X5", "X4", "X5"),
                         byrow = TRUE, ncol = 2, dimnames = list(NULL, c("from", "to")))

simulate <- function(n) {
  e <- matrix(rnorm(5 * n), n, 5)
  x1 <- e[, 1]
  x2 <- -0.6 * x1 + e[, 2]
  x3 <- -0.7 * x1 + e[, 3]
  x4 <- -0.7 * x2 + 0.9 * x3 + e[, 4]
  x5 <- 0.9 * x3 - 0.8 * x4 + e[, 5]
  data.frame(X1 = x1, X2 = x2, X3 = x3, X4 = x4, X5 = x5)
}

sizes <- c(25, 50, 100, 200, 400, 800, 1600, 3200)
reps <- 200
res <- t(sapply(sizes, function(n) {
  out <- replicate(reps, {
    fit <- pc.stable(simulate(n), test = "zf", alpha = 0.05)
    c(skeleton = all.equal(skeleton(fit), skeleton(true_dag)) == TRUE,
      cpdag = all.equal(fit, cpdag(true_dag)) == TRUE,
      shd = shd(skeleton(fit), skeleton(true_dag)))
  })
  rowMeans(out)
}))
res <- data.frame(n = sizes, res)
print(res)

op <- par(mfrow = c(1, 2))
plot(res$n, res$skeleton, type = "b", log = "x", ylim = c(0, 1),
     xlab = "sample size n", ylab = "proportion correct")
lines(res$n, res$cpdag, type = "b", lty = 2, pch = 2)
legend("bottomright", c("skeleton", "CPDAG"), lty = 1:2, pch = 1:2)
plot(res$n, res$shd, type = "b", log = "x", col = "red",
     xlab = "sample size n", ylab = "mean wrong skeleton edges")
par(op)
