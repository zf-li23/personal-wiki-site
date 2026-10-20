# Residual plot and normal Q-Q plot of the residuals for the Pisa regression.
year <- 75:87
lean <- c(642, 644, 656, 667, 673, 688, 696, 698, 713, 717, 725, 742, 757)

fit <- lm(lean ~ year)
e <- residuals(fit)

op <- par(mfrow = c(1, 2))
plot(year, e, pch = 19, col = "steelblue", xlab = "year (19xx)", ylab = "residual",
     main = "Residuals against the predictor")
abline(h = 0)

qqnorm(e, pch = 19, col = "steelblue", main = "Normal Q-Q plot of the residuals",
       xlab = "standard normal quantile", ylab = "ordered residual")
qqline(e, col = "firebrick", lwd = 1.5)   # line through the quartiles
par(op)
