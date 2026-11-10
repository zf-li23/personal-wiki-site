# Cox-Stuart test for the annual mileages of cars and trucks, 1970-83.
years <- 1970:1983
cars <- c(9.8, 9.9, 10.0, 9.8, 9.2, 9.4, 9.5, 9.6, 9.8, 9.3, 8.9, 8.7, 9.2, 9.3)
trucks <- c(11.5, 11.5, 12.2, 11.5, 10.9, 10.6, 11.1, 11.1, 11.0, 10.8, 11.4, 12.3, 11.2, 11.2)

cox_stuart <- function(x) {
  n <- length(x)
  m <- n %/% 2
  first <- x[1:m]
  second <- x[(n - m + 1):n]          # drops the middle value when n is odd
  d <- second - first
  d <- d[d != 0]                       # ties carry no information
  binom.test(sum(d > 0), length(d))
}
print(cox_stuart(cars))                # 0 plus, 7 minus: p = 0.0156
print(cox_stuart(trucks))              # 3 plus, 4 minus: p = 1

op <- par(mfrow = c(1, 2))
for (s in list(list("Cars", cars), list("Trucks", trucks))) {
  x <- s[[2]]; m <- length(x) %/% 2
  plot(years, x, type = "b", pch = 19, col = "gray40",
       xlab = "year", ylab = "mean annual mileage (thousand miles)", main = s[[1]])
  d <- x[(m + 1):(2 * m)] - x[1:m]
  arrows(years[1:m], x[1:m], years[(m + 1):(2 * m)], x[(m + 1):(2 * m)],
         length = 0.08, col = ifelse(d > 0, "steelblue", "firebrick"))
  abline(v = years[m] + 0.5, lty = 3)
}
par(op)
