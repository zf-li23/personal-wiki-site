# Impurity experiment without replication: interaction plot, additive ANOVA, Tukey's test.
impurity <- c(5, 4, 6, 3, 5, 3, 1, 4, 2, 3, 1, 1, 3, 1, 2)
temp <- factor(rep(c(100, 125, 150), each = 5))
press <- factor(rep(c(25, 30, 35, 40, 45), 3))
interaction.plot(press, temp, impurity, xlab = "pressure (psi)", ylab = "impurity",
                 trace.label = "temperature", bty = "L")
summary(aov(impurity ~ temp + press))        # additive model
library(additivityTests)
response <- matrix(impurity, nrow = nlevels(temp), byrow = TRUE)
tukey.test(response)
