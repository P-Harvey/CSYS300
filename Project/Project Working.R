# Patrick L. Harvey
# CSYS 300
# Project (DRAFT)
# 20210929

library(ggplot2)
library(ggExtra)
library(hrbrthemes)
library(tidymodels)
library(tidyverse)
library(extrafont)
library(broom)
library(latex2exp)
library(hexbin)
library(RColorBrewer)
library(stats)

hrbrthemes::import_roboto_condensed()

#setwd("C:/Users/pharv/Desktop/CSYS 300 (Principles of Complex Systems)")

fancy_scientific <- function(l) {
  # turn in to character string in scientific notation
  l <- format(l, scientific = TRUE)
  # quote the part before the exponent to keep all the digits
  l <- gsub("^(.*)e", "'\\1'e", l)
  # turn the 'e+' into plotmath format
  l <- gsub("e", "%*%10^", l)
  # return this as an expression
  parse(text=l)
}

pop_10 <- read.csv(file = 'Project/2010 Pop.csv', header = FALSE)
pop_18 <- read.csv(file = 'Project/2018 Pop.csv', header = FALSE)
insec_12_14 <- read.csv(file = 'Project/FOODINSEC 12 14.csv', header = FALSE)
insec_15_17 <- read.csv(file = 'Project/FOODINSEC 15 17.csv', header = FALSE)

pop_df <- data.frame(x=pop_10$V5, y=pop_18$V5)
pop_fit <- lm(pop_df$y ~ pop_df$x)

insec_df <- data.frame(x=insec_12_14$V5, y=insec_15_17$V5)
insec_fit <- lm(insec_df$y ~ insec_df$x)

hist(log10(pop_10$V5))
hist(log10(pop_18$V5))
plot(log10(pop_df))

hist(log10(insec_12_14$V5))
hist(log10(insec_15_17$V5))
plot(log10(insec_df))

# Create data
x <- insec_df$x
y <- insec_df$y

p <- ggplot(
  pop_df, 
  aes(x=log10(x), y=log10(y))) +
  geom_point(shape='o') +
  theme_ipsum_rc()
p