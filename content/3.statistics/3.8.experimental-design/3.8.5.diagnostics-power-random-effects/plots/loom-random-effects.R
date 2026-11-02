# Fabric strength on four randomly chosen looms: random-effects analysis.
LoomData <- data.frame(Loom = factor(rep(1:4, each = 4)),
                       Obs = c(98, 97, 99, 96, 91, 90, 93, 92, 96, 95, 97, 95, 95, 96, 99, 98))
tab <- summary(aov(Obs ~ Loom, data = LoomData))[[1]]
ms <- tab[["Mean Sq"]]; n <- 4
s2 <- ms[2]; st2 <- (ms[1] - ms[2]) / n
c(sigma2 = s2, sigma2_tau = st2, ICC = st2 / (st2 + s2))
library(lme4)
summary(lmer(Obs ~ (1 | Loom), data = LoomData))
m <- tapply(LoomData$Obs, LoomData$Loom, mean)
stripchart(Obs ~ Loom, data = LoomData, vertical = TRUE, pch = 19, col = "steelblue",
           xlab = "loom", ylab = "strength", main = "Fiber strength: ICC = 0.79")
segments(1:4 - 0.3, m, 1:4 + 0.3, m, lwd = 2, col = "steelblue")
abline(h = mean(LoomData$Obs), lty = 2, col = "darkorange")
