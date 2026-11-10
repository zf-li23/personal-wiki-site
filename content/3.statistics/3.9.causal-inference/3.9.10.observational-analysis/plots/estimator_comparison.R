# Sampling distributions of estimators of an average effect in simulated observational studies.
set.seed(0)
n <- 1000; reps <- 300; tau <- 2

one_run <- function() {
  x1 <- rnorm(n); x2 <- rnorm(n)
  w <- rbinom(n, 1, plogis(-0.8 + 1.2 * x1 + 0.6 * x2))
  y <- 1.5 * x1 + 0.8 * x1^2 + x2 + tau * w + rnorm(n)   # constant effect: ATE = ATT = tau
  d <- data.frame(y, w, x1, x2)
  e <- fitted(glm(w ~ x1 + x2, family = binomial, data = d))
  ipw <- weighted.mean(y[w == 1], 1 / e[w == 1]) - weighted.mean(y[w == 0], 1 / (1 - e[w == 0]))
  d$block <- cut(e, quantile(e, 0:5 / 5), include.lowest = TRUE)
  by_block <- sapply(split(d, d$block), function(b)
    c(q = nrow(b) / n, dif = mean(b$y[b$w == 1]) - mean(b$y[b$w == 0]),
      adj = coef(lm(y ~ w + x1 + x2, data = b))[["w"]]))
  xt <- cbind(x1, x2)[w == 1, ]; xc <- cbind(x1, x2)[w == 0, ]; yc <- y[w == 0]
  m <- apply(xt, 1, function(r) which.min(colSums((t(xc) - r)^2)))   # nearest control, with replacement
  used <- unique(m)
  beta <- coef(lm(yc[used] ~ xc[used, ]))[-1]
  c("difference in means" = mean(y[w == 1]) - mean(y[w == 0]),
    "regression" = coef(lm(y ~ w + x1 + x2))[["w"]],
    "weighting (IPW)" = ipw,
    "5 blocks" = sum(by_block["q", ] * by_block["dif", ]),
    "5 blocks + regression" = sum(by_block["q", ] * by_block["adj", ]),
    "matching" = mean(y[w == 1] - yc[m]),
    "bias-corrected matching" = mean(y[w == 1] - yc[m] - (xt - xc[m, ]) %*% beta))
}

res <- t(replicate(reps, one_run()))
par(mar = c(4.5, 11, 1, 1))
boxplot(res[, ncol(res):1], horizontal = TRUE, las = 1, outline = FALSE,
        xlab = sprintf("estimate over %d simulated data sets (N = %d)", reps, n))
abline(v = tau, lty = 2, col = "firebrick")
