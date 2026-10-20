# Interaction plot of the bakery data and schematic patterns without and with interaction.
sales <- c(47, 43, 62, 68, 41, 39,    # regular width: bottom, middle, top (two stores each)
           46, 40, 67, 71, 42, 46)    # wide
width <- factor(rep(c("regular width", "wide"), each = 6))
height <- factor(rep(rep(c("bottom", "middle", "top"), each = 2), times = 2),
                 levels = c("bottom", "middle", "top"))

fit <- aov(sales ~ height * width)
print(summary(fit))

op <- par(mfrow = c(1, 3))
interaction.plot(height, width, sales, type = "b", pch = c(19, 15), lty = c(2, 1), lwd = 1.8,
                 col = c("steelblue", "darkorange"), legend = TRUE, trace.label = "",
                 xlab = "shelf height (factor A)", ylab = "cases of bread sold",
                 main = "Bakery data: nearly parallel")
points(as.numeric(height) + ifelse(width == "wide", 0.05, -0.05), sales,
       col = adjustcolor(c("steelblue", "darkorange")[as.numeric(width)], 0.5), pch = 19, cex = 0.8)

x <- 1:3
matplot(x, cbind(c(9, 11, 13), c(3, 5, 7)), type = "b", pch = c(19, 15), lty = c(1, 2), lwd = 1.8,
        col = c("steelblue", "darkorange"), ylim = c(0, 16), xaxt = "n",
        xlab = "level of factor A", ylab = "mean response", main = "No interaction: parallel lines")
axis(1, at = x)
legend("topleft", bty = "n", pch = c(19, 15), lty = c(1, 2), col = c("steelblue", "darkorange"),
       legend = c("B level 1", "B level 2"))

matplot(x, cbind(c(4, 8, 12), c(12, 8, 4), c(8, 8, 8)), type = "b", pch = c(19, 15, NA), lty = c(1, 2, 3),
        lwd = c(1.8, 1.8, 1.5), col = c("steelblue", "darkorange", "gray"), ylim = c(0, 16), xaxt = "n",
        xlab = "level of factor A", ylab = "mean response", main = "Crossing interaction")
axis(1, at = x)
legend("topleft", bty = "n", pch = c(19, 15, NA), lty = c(1, 2, 3), col = c("steelblue", "darkorange", "gray"),
       legend = c("B level 1", "B level 2", "marginal means of A"))
par(op)
