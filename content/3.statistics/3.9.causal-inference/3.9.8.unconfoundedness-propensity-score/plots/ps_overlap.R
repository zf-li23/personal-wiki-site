# Estimated propensity score and linearized propensity score by treatment group (simulated data).
set.seed(0)
n <- 3000
x1 <- rnorm(n); x2 <- rnorm(n); x3 <- rbinom(n, 1, 0.4)
logit <- -2.2 + 1.6 * x1 + 0.8 * x2 + 0.9 * x3 + 0.3 * x1 * x2
w <- rbinom(n, 1, plogis(logit))

fit <- glm(w ~ x1 + x2 + x3 + x1:x2, family = binomial)
e_hat <- fitted(fit)
l_hat <- qlogis(e_hat)          # log(e / (1 - e))

par(mfrow = c(1, 2))
for (v in list(list(e_hat, "estimated propensity score", seq(0, 1, length.out = 41)),
               list(l_hat, "linearized propensity score",
                    seq(min(l_hat), max(l_hat), length.out = 41)))) {
  hc <- hist(v[[1]][w == 0], breaks = v[[3]], plot = FALSE)
  ht <- hist(v[[1]][w == 1], breaks = v[[3]], plot = FALSE)
  plot(hc, freq = FALSE, col = adjustcolor("steelblue", 0.5), border = "white",
       ylim = c(0, max(hc$density, ht$density)), xlab = v[[2]], main = "")
  plot(ht, freq = FALSE, col = adjustcolor("firebrick", 0.5), border = "white", add = TRUE)
  legend("topright", c("control", "treated"),
         fill = adjustcolor(c("steelblue", "firebrick"), 0.5), bty = "n")
}
