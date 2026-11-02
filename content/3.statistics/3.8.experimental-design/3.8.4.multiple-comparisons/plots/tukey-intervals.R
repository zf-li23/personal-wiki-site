# Tukey simultaneous 95% intervals and individual LSD intervals for the etching data.
y <- c(575, 542, 530, 539, 570,
       565, 593, 590, 579, 610,
       600, 651, 610, 637, 629,
       725, 700, 715, 685, 710)
RF <- factor(rep(c(160, 180, 200, 220), each = 5))
mod <- aov(y ~ RF)
tk <- TukeyHSD(mod)$RF
print(tk)

mse <- deviance(mod) / df.residual(mod)
lsd <- qt(0.975, df.residual(mod)) * sqrt(2 * mse / 5)
g <- nrow(tk)
plot(NA, xlim = range(tk[, "lwr"], tk[, "upr"]), ylim = c(g + 0.5, 0.5), yaxt = "n",
     xlab = "difference of mean etch rates (Angstrom/min)", ylab = "",
     main = "Pairwise differences of the etching means, 95% intervals")
axis(2, at = 1:g, labels = rownames(tk), las = 1)
abline(v = 0, col = "gray")
segments(tk[, "lwr"], 1:g - 0.15, tk[, "upr"], 1:g - 0.15, col = "steelblue", lwd = 3)
segments(tk[, "diff"] - lsd, 1:g + 0.15, tk[, "diff"] + lsd, 1:g + 0.15, col = "darkorange", lwd = 3)
legend("bottomright", bty = "n", col = c("steelblue", "darkorange"), lwd = 3,
       legend = c("Tukey HSD", "LSD (unadjusted)"))
