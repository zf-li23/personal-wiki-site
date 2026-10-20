# One model with a dummy variable and an interaction gives two regression lines.
set.seed(0)
n <- 40
age <- runif(2 * n, 24, 144)
boy <- rep(c(0, 1), each = n)
height <- 78 + 0.52 * age + 1.5 * boy + 0.04 * age * boy + 3.5 * rnorm(2 * n)

fit <- lm(height ~ age * boy)   # columns 1, age, boy, age:boy
b <- coef(fit)
print(summary(fit))

plot(age, height, type = "n", xlim = c(20, 150), xlab = "age in months X_1", ylab = "height (cm)",
     main = sprintf("fit: girls  %.1f + %.3f X_1;   boys  %.1f + %.3f X_1",
                    b[1], b[2], b[1] + b[3], b[2] + b[4]), cex.main = 0.9)
points(age[boy == 0], height[boy == 0], pch = 19, cex = 0.8, col = "firebrick")
points(age[boy == 1], height[boy == 1], pch = 15, cex = 0.8, col = "steelblue")
abline(a = b[1], b = b[2], col = "firebrick", lwd = 1.8)
abline(a = b[1] + b[3], b = b[2] + b[4], col = "steelblue", lwd = 1.8)
legend("topleft", bty = "n", pch = c(19, 15), col = c("firebrick", "steelblue"),
       legend = c("girls (X_2 = 0)", "boys (X_2 = 1)"))
