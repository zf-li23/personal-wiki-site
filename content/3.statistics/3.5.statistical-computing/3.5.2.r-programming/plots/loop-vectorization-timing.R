# Run time of three ways to fill a vector of n results.
grow <- function(x) {
  out <- NULL
  for (v in x) out <- c(out, v * v)        # copies the whole vector every time
  out
}
prealloc <- function(x) {
  out <- numeric(length(x))                # allocate once
  for (i in seq_along(x)) out[i] <- x[i] * x[i]
  out
}
vectorized <- function(x) x * x

best_time <- function(f, x, reps = 3) {
  min(replicate(reps, system.time(f(x))[["elapsed"]]))
}

ns <- unique(round(10^seq(2, 5, length.out = 10)))
set.seed(0)
times <- t(sapply(ns, function(n) {
  x <- runif(n)
  c(grow = best_time(grow, x, reps = if (n > 20000) 1 else 3),
    prealloc = best_time(prealloc, x),
    vectorized = best_time(vectorized, x))
}))
times[times == 0] <- NA                   # below the timer resolution
matplot(ns, times, log = "xy", type = "b", pch = c(19, 15, 17), lty = 1,
        col = c("steelblue", "darkorange", "forestgreen"),
        xlab = "vector length n", ylab = "seconds",
        main = "Growing a vector costs O(n^2) copies")
legend("topleft", bty = "n", cex = 0.8, legend = c("grow inside the loop", "preallocated loop", "vectorized"),
       col = c("steelblue", "darkorange", "forestgreen"), pch = c(19, 15, 17), lty = 1)
