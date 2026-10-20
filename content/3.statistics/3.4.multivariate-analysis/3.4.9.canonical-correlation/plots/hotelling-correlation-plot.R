# Hotelling's reading/arithmetic example: variables plotted by their correlations with U_1 and U_2.
Sigma <- matrix(c(100, 60, 30, 7.2,
                  60, 100, -6, 8.4,
                  30, -6, 144, 57.6,
                  7.2, 8.4, 57.6, 144), 4, 4, byrow = TRUE)
vars <- c("reading speed", "reading power", "arithmetic speed", "arithmetic power")

# Symmetric matrix power via the spectral decomposition.
mpow <- function(A, k) {
  e <- eigen(A, symmetric = TRUE)
  e$vectors %*% diag(e$values^k) %*% t(e$vectors)
}

S11 <- Sigma[1:2, 1:2]
S12 <- Sigma[1:2, 3:4]
S22 <- Sigma[3:4, 3:4]
s <- svd(mpow(S11, -0.5) %*% S12 %*% mpow(S22, -0.5))
rho <- s$d                               # canonical correlations
A <- t(mpow(S11, -0.5) %*% s$u)          # rows: coefficient vectors of U_1, U_2
sds <- sqrt(diag(Sigma))
corr <- sweep(A %*% Sigma[1:2, ], 2, sds, "/")  # Corr(U_k, X_i) for all four variables

tt <- seq(0, 2 * pi, length.out = 300)
plot(NA, xlim = c(-1.1, 1.1), ylim = c(-1.1, 1.1), asp = 1,
     xlab = sprintf("correlation with U_1  (rho_1* = %.2f)", rho[1]),
     ylab = sprintf("correlation with U_2  (rho_2* = %.2f)", rho[2]),
     main = "Variables in the plane of the first-set canonical variates")
lines(cos(tt), sin(tt), col = "gray50")
abline(h = 0, v = 0, col = "gray70")
cols <- rep(c("steelblue", "firebrick"), each = 2)
arrows(0, 0, corr[1, ], corr[2, ], col = cols, lwd = 1.6, length = 0.1)
text(corr[1, ], corr[2, ], labels = vars, col = cols, pos = c(4, 4, 2, 3), cex = 0.85)
