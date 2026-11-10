# Empirical distribution functions of saliva production for 7 women and 21 men, and the Smirnov distance.
fe <- c(0.45, 0.60, 0.80, 0.85, 0.95, 1.00, 1.75)
ma <- c(0.40, 0.50, 0.55, 0.65, 0.70, 0.75, 0.90, 1.05, 1.15, 1.25, 1.30,
        1.35, 1.45, 1.50, 1.85, 1.90, 2.30, 2.55, 2.70, 2.85, 3.85)
print(ks.test(fe, ma))                              # D = 0.5238, exact p = 0.093
print(ks.test(fe, ma, alternative = "greater"))     # D^+ = 0.5238
Ff <- ecdf(fe); Fm <- ecdf(ma)
grid <- sort(c(fe, ma))
k <- which.max(abs(Ff(grid) - Fm(grid)))
plot(Ff, do.points = FALSE, verticals = TRUE, col = "firebrick", lwd = 2, xlim = c(0.2, 4),
     main = "Smirnov test, saliva data", xlab = "saliva production (ml/min)", ylab = "EDF")
plot(Fm, do.points = FALSE, verticals = TRUE, col = "steelblue", lwd = 2, add = TRUE)
segments(grid[k], Fm(grid[k]), grid[k], Ff(grid[k]), lwd = 3)
legend("bottomright", c("women", "men"), col = c("firebrick", "steelblue"), lwd = 2, bty = "n")
