# Dairy cow crossover experiment: profiles by cow and the ANOVAs with and without carryover.
Diet <- data.frame(
  Treat  = factor(c("A", "B", "C", "A", "B", "C", "B", "C", "A",
                    "C", "A", "B", "C", "A", "B", "B", "C", "A")),
  Period = factor(rep(1:3, each = 6)),
  Cow    = factor(rep(1:6, times = 3)),
  Yield  = c(38, 109, 124, 86, 75, 101, 25, 86, 72, 76, 35, 63, 15, 39, 27, 46, 34, 1))
interaction.plot(Diet$Period, Diet$Cow, Diet$Yield, xlab = "Period",
                 ylab = "Milk yield", trace.label = "Cow", bty = "L")
summary(aov(Yield ~ ., Diet))                              # Case 2: periods common to both squares
Diet$Square <- factor(rep(c(1, 2), each = 3))                # cows 1-3 and 4-6
summary(aov(Yield ~ Treat + Cow + Square/Period, Diet))    # Case 3: periods nested in squares
# Carryover: treatment received in the previous period ("0" in period 1)
prev <- c(rep("0", 6), as.character(Diet$Treat[1:12]))
Diet$ResTrt <- factor(prev)
anova(lm(Yield ~ Period + Cow + Treat + ResTrt, Diet))   # carryover adjusted for direct effects
anova(lm(Yield ~ Period + Cow + ResTrt + Treat, Diet))   # direct effects adjusted for carryover
