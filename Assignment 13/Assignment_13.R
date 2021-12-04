library(ggplot2)
library(latex2exp)
library(hrbrthemes)
hrbrthemes::import_roboto_condensed()

gamma <- 2.16096

theta_wealth <- function(theta_pop) {
  1-(1-theta_pop)^((gamma-2)/(gamma-1))
}

x <- (0:1000)/1000
y <- theta_wealth(x)

dfline <- data.frame(x=x, y=x)

dfplot <- data.frame(theta_pop=100*x, theta_wealth=100*y)

ggplot(dfplot, aes(x, y)) + 
  geom_line() +
  geom_line(dfline, color="red", mapping = aes()) +
  labs(x=TeX("Bottom Population Proportion $\\theta_{pop}$"),
       y=TeX("Wealth Proportion $\\theta_{wealth}$"),
       title="Proportion of Wealth held by Proporiton Population",
       subtitle=TeX("$\\gamma$=2.16096")) +
  theme_ipsum_rc()
