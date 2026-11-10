# Coronary deaths of British male doctors by age and smoking: age-specific death rates and rate ratios.
d <- data.frame(age = factor(rep(c("35-44", "45-54", "55-64", "65-74", "75-84"), 2)),
                smoke = factor(rep(c("smoker", "non-smoker"), each = 5), levels = c("non-smoker", "smoker")),
                deaths = c(32, 104, 206, 186, 102, 2, 12, 28, 28, 31),
                py = c(52407, 43248, 28612, 12663, 5317, 18790, 10673, 5710, 2585, 1462))
d$rate <- d$deaths / d$py * 1e5
add <- glm(deaths ~ age + smoke, offset = log(py), family = poisson, data = d)
int <- glm(deaths ~ age * smoke, offset = log(py), family = poisson, data = d)
print(anova(add, int, test = "Chisq"))                  # deviance 12.13 on 4 df, p = 0.016
rr <- with(d, rate[smoke == "smoker"] / rate[smoke == "non-smoker"])
se <- with(d, sqrt(1 / deaths[smoke == "smoker"] + 1 / deaths[smoke == "non-smoker"]))
op <- par(mfrow = c(1, 2))
interaction.plot(d$age, d$smoke, d$rate, log = "y", type = "b", pch = 19,
                 xlab = "age group", ylab = "deaths per 100,000 person-years", trace.label = "")
plot(1:5, rr, log = "y", pch = 19, ylim = range(rr * exp(-2 * se), rr * exp(2 * se)), xaxt = "n",
     xlab = "age group", ylab = "rate ratio")
arrows(1:5, rr * exp(-1.96 * se), 1:5, rr * exp(1.96 * se), angle = 90, code = 3, length = 0.05)
axis(1, 1:5, levels(d$age)); abline(h = 1, lty = 3)
par(op)
