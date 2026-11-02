# Twin data analysed as two independent groups and as pairs.
drug1 <- c(3, 3, 4, 8, 3, 2, 9, 5, 4, 7)
drug2 <- c(3, 5, 3, 8, 2, 4, 9, 4, 5, 6)
t.test(drug1, drug2, var.equal = TRUE)   # unpaired: t = -0.097, df = 18
t.test(drug1, drug2, paired = TRUE)      # paired:   t = -0.264, df = 9

par(mfrow = c(1, 2))
stripchart(list("drug 1" = drug1, "drug 2" = drug2), vertical = TRUE, method = "jitter",
           pch = 19, col = c("steelblue", "darkorange"), ylab = "response",
           main = "Unpaired view", xlim = c(0.5, 2.5))
segments(c(0.75, 1.75), c(mean(drug1), mean(drug2)), c(1.25, 2.25), col = c("steelblue", "darkorange"),
         lwd = 2)
plot(NA, xlim = c(0.5, 2.5), ylim = range(c(drug1, drug2)), xaxt = "n", xlab = "", ylab = "response",
     main = "Paired view")
axis(1, at = 1:2, labels = c("drug 1", "drug 2"))
segments(1, drug1, 2, drug2, col = "gray")
points(rep(1, 10), drug1, pch = 19, col = "steelblue")
points(rep(2, 10), drug2, pch = 19, col = "darkorange")
