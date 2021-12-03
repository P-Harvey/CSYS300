gamma = 2.6096
n <- 330000000
c <- n*(gamma-1)*(1.01^(gamma-1))
x <- 1.01:10^8

N_x <- function(y) {
  c*y^(-gamma)
}

y = N_x(x)

df <- data.frame(x=x,y=y)
rm(x,y)
s = df[sample(nrow(df), 10000), ]

sort_s <- s[order(s$x),]
anno <- sum(sort_s$x[1:2500])/sum(sort_s$x)
less_than <- 1-sum(sort_s$y[1:2500])

plot(log10(s$y), log10(s$x),
     main="Wealth Distribution: Gamma = 2.6096 \n 10,000 samples from 10^8 observations",
     xlab="Proportion of Wealth (Log 10)",
     ylab="Count of Population (Log 10)")
text(-9.8,7.75, expression(N(x)~"="~cx^-2.6096))
text(-6,7, paste("Proportion of population with less \n than", 
       signif(less_than,digits=4), "of wealth = ", 
       signif(anno, digits=4), sep=" "))