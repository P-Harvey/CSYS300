library(ggplot2)
library(hrbrthemes)
hrbrthemes::import_roboto_condensed()

setwd("./Assignments Complete/")

words_download <- read.table("words_download.txt",
                             header = FALSE)

k <- words_download$V1
Nk <- words_download$V2
log10k <- log10(k)
log10Nk <- log10(Nk)

data <- data.frame(x=log10k, y=log10Nk)

hypothetical <- function(l_k) {
  l_n_k <- (3.46*(10^8)*l_k^(-0.661))/l_k
}

h_k = 1:199
h_Nk = hypothetical(h_k)

data2 <- data.frame(x=log10(h_k), y=log10(h_Nk))

dm = mean(10^(data2$y))
dv = var(10^(data2$y))

(out <- ggplot(data, aes(x, y)) +
    geom_point() +
    geom_point(data = data2,color='red') +
    labs(x="Log10 Word Frequency (k)", y="Log10 Word Count (Nk)",
         title="Google Word Frequency Versus Count",
         subtitle="CSYS300 Assignment 11",
         caption = paste("Red Points indicate hypothetical k v. Nk",
           "\nHypothetical Mean(Nk) = ",signif(dm,5),
           "\nHypothetical Variance(Nk) =",signif(dv,5))) +
    coord_fixed() +
    theme_ipsum_rc()
)

h_f = 1
h_C = (hypothetical(h_f))

frac_word_once <- 6.9*10^(-20)
tot_uniq_word <- 5*10^27
from_1_199 <- 19900
from_1_199/tot_uniq_word
