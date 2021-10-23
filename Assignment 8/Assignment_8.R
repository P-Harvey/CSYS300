library(ggplot2)
library(hrbrthemes)
library(tidyverse)
library(extrafont)
library(broom)
library(latex2exp)
library(stats)

hrbrthemes::import_roboto_condensed()

gamma = 3/2
N <- 1:10^6
k <- 1:10^8
P_k <- k^(-gamma)
K_1 <- c()
K_2 <- c()
K_3 <- c()
K_4 <- c()
K_5 <- c()
K_6 <- c()
for (i in 1:1000) {
  N_1 <- sample(P_k, 10, replace = FALSE, prob = NULL)
  K_1 <- append(K_1, max(N_1), after = length(K_1))
  N_2 <- sample(P_k, 10^2, replace = FALSE, prob = NULL)
  K_2 <- append(K_2, max(N_2), after = length(K_2))
  N_3 <- sample(P_k, 10^3, replace = FALSE, prob = NULL)
  K_3 <- append(K_3, max(N_3), after = length(K_3))
  N_4 <- sample(P_k, 10^4, replace = FALSE, prob = NULL)
  K_4 <- append(K_4, max(N_4), after = length(K_4))
  N_5 <- sample(P_k, 10^5, replace = FALSE, prob = NULL)
  K_5 <- append(K_5, max(N_5), after = length(K_5))
  N_6 <- sample(P_k, 10^6, replace = FALSE, prob = NULL)
  K_6 <- append(K_6, max(N_6), after = length(K_6))
}
rm(P_k)
P_1 <- plot(1:1000, 
            sort(K_1, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10; 1,000 iterations'
            )
P_2 <- plot(1:1000, 
            sort(K_2, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10^2; 1,000 iterations'
            )
P_3 <- plot(1:1000, 
            sort(K_3, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10^3; 1,000 iterations'
            )
P_4 <- plot(1:1000, 
            sort(K_4, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10^4; 1,000 iterations'
            )
P_5 <- plot(1:1000, 
            sort(K_5, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10^5; 1,000 iterations'
            )
P_6 <- plot(1:1000, 
            sort(K_6, decreasing = TRUE), 
            log="xy",
            xlab = 'n',
            ylab = 'K Max',
            main = 'K_max for N = 10^6; 1,000 iterations'
            )
m1 <- c(mean(K_1), mean(K_2), mean(K_3),
        mean(K_4), mean(K_5), mean(K_6))

df <- data.frame(x=sort(m1), y=c(10, 10^2, 10^3, 10^4, 10^5, 10^6))
fit <- lm(log10(df$y)~log10(df$x))
summary(fit)
slope <- log10(cor(df$x, df$y) * (sd(df$y) / sd(df$x)))
A_1 <- plot(df, 
            log="xy",
            xlab = 'N',
            ylab = '<K Max>',
            main = 'Average K_max from N=10 to N=10^6 over 1,000 iterations'
) +
  abline(coef(fit[1:2])) +
  text(10^-5,10^2.5, labels="Slope: 0.59105")
