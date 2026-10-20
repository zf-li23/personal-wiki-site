# Geometric probability: the meeting problem on the unit square, |x - y| <= 1/4, checked by simulation.
set.seed(0)
t0 <- 0.25
pts <- matrix(runif(800), ncol = 2)
inside <- abs(pts[, 1] - pts[, 2]) <= t0

plot(NA, xlim = c(0, 1), ylim = c(0, 1), asp = 1,
     xlab = "delay of first person x (hours)", ylab = "delay of second person y (hours)",
     main = sprintf("area(M) = 7/16 = 0.4375, simulated: %.3f", mean(inside)))
polygon(c(0, t0, 1, 1, 1 - t0, 0), c(0, 0, 1 - t0, 1, 1, t0),
        col = adjustcolor("steelblue", 0.35), border = "steelblue", lwd = 1.5)
rect(0, 0, 1, 1, lwd = 1.2)
points(pts[inside, ], pch = 19, cex = 0.4, col = "steelblue")
points(pts[!inside, ], pch = 19, cex = 0.4, col = "firebrick")
legend("topleft", bty = "n", cex = 0.8, pch = c(15, 19, 19),
       col = c(adjustcolor("steelblue", 0.35), "steelblue", "firebrick"),
       legend = c("M: |x - y| <= 1/4", "simulated: meet", "simulated: miss"))
