# Battery life experiment: interaction plot and two-way ANOVA.
Battery <- data.frame(
  Type = factor(rep(1:3, each = 12)),
  Temp = factor(rep(rep(c(15, 70, 125), each = 4), 3)),
  Life = c(130, 155, 74, 180, 34, 40, 80, 75, 20, 70, 82, 58,
           150, 188, 159, 126, 136, 122, 106, 115, 25, 70, 58, 45,
           138, 110, 168, 160, 174, 120, 150, 139, 96, 104, 82, 60))
summary(aov(Life ~ Type * Temp, data = Battery))
interaction.plot(x.factor = Battery$Temp, trace.factor = Battery$Type,
                 response = Battery$Life, xlab = "Temperature",
                 ylab = "Average life", trace.label = "Material Type", bty = "L")
