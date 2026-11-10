# Naive analyses and the IV (Wald) estimator in a randomized experiment with noncompliance.
set.seed(0)
n <- 2000; reps <- 500
effects <- c(nt = 0.5, co = 1, at = 4)

one_study <- function() {
  u <- rnorm(n)                                   # unobserved health
  score <- u + rnorm(n)
  g <- ifelse(score < -0.6, "nt", ifelse(score < 0.9, "co", "at"))
  z <- seq_len(n) %in% sample(n, n / 2)           # randomized assignment
  w <- g == "at" | (g == "co" & z)                # receipt of treatment (no defiers)
  tau_i <- effects[g] + rnorm(n, 0, 0.5)
  y <- 1 + 1.5 * u + rnorm(n) + w * tau_i         # z affects y only through w
  itt_y <- mean(y[z]) - mean(y[!z]); itt_w <- mean(w[z]) - mean(w[!z])
  c("as treated" = mean(y[w]) - mean(y[!w]),
    "per protocol" = mean(y[w & z]) - mean(y[!w & !z]),
    "intention to treat" = itt_y,
    "IV (Wald)" = itt_y / itt_w,
    cace = mean(tau_i[g == "co"]), ate = mean(tau_i))
}

res <- t(replicate(reps, one_study()))
par(mar = c(4.5, 9, 1, 1))
boxplot(res[, 4:1], horizontal = TRUE, las = 1, outline = FALSE,
        xlab = sprintf("estimate over %d simulated experiments (N = %d)", reps, n))
abline(v = mean(res[, "cace"]), lty = 2, col = "firebrick")
abline(v = mean(res[, "ate"]), lty = 3, col = "steelblue")
legend("bottomright", c("complier effect", "population average effect"),
       lty = c(2, 3), col = c("firebrick", "steelblue"), bty = "n")
