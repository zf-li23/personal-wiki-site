# Pulse rates of seven students on three occasions: raw profiles and within-block ranks for the Friedman test.
pr <- matrix(c(72, 120, 76, 96, 120, 95, 88, 132, 104, 92, 120, 96,
               74, 101, 84, 76, 96, 72, 82, 112, 76), ncol = 3, byrow = TRUE,
             dimnames = list(LETTERS[1:7], c("I", "II", "III")))
print(friedman.test(pr))                                  # chi-squared = 10.571, p = 0.005063
ranks <- t(apply(pr, 1, rank))
print(colSums(ranks))                                     # 10 21 11
op <- par(mfrow = c(1, 2))
matplot(t(pr), type = "b", pch = 19, lty = 1, col = "steelblue", xaxt = "n",
        ylab = "pulse rate", main = "Seven students")
axis(1, 1:3, colnames(pr))
matplot(t(ranks), type = "b", pch = 19, lty = 1, col = "darkorange", xaxt = "n",
        ylab = "rank within student", main = "Within-block ranks")
axis(1, 1:3, colnames(pr))
par(op)
