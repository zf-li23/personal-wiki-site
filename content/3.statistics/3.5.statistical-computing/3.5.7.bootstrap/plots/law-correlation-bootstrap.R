# Bootstrap distribution of the sample correlation for the law school data (15 schools),
# with the normal, basic, percentile and BCa 95% intervals from boot.ci.
library(bootstrap)  # data set law
library(boot)

set.seed(0)
r <- function(x, i) cor(x$LSAT[i], x$GPA[i])
obj <- boot(data = law, statistic = r, R = 2000)
obj                       # original value, bootstrap bias and standard error
ci <- boot.ci(obj, type = c("norm", "basic", "perc", "bca"))
ci

hist(obj$t, breaks = 50, freq = FALSE, col = "lightsteelblue", border = "white",
     xlim = c(0, 1.45), xlab = "bootstrap correlation r*",
     main = sprintf("Law school data: bootstrap se = %.3f", sd(obj$t)))
abline(v = obj$t0, col = "firebrick", lwd = 2)
ends <- rbind(ci$normal[2:3], ci$basic[4:5], ci$percent[4:5], ci$bca[4:5])
cols <- c("darkorange", "forestgreen", "purple", "brown")
top <- par("usr")[4]
for (k in 1:4) {
  y <- top * (0.92 - 0.08 * (k - 1))
  segments(ends[k, 1], y, ends[k, 2], y, col = cols[k], lwd = 3)
}
legend("left", bty = "n", cex = 0.8, lwd = 3, col = c("firebrick", cols),
       legend = c("sample correlation", "normal", "basic", "percentile", "BCa"))
