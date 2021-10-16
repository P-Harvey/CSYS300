# PATRICK L HARVEY
# plharvey@uvm.edu
# CSYS-300 Fall 2021
# Assignment 6.6

from string import punctuation
import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
from matplotlib import pyplot as plt
from scipy import special as sp
from sklearn.linear_model import LinearRegression


def words_of_book(book):
    """Download `A tale of two cities` from Project Gutenberg. Return a list of
    words. Punctuation has been removed and upper-case letters have been
    replaced with lower-case.
    """
    
    with open(book) as f:
        raw = f.readlines()
    # Loop over every character in the string, keep it only if it is NOT
    # punctuation:
    exclude = set(punctuation) # Keep a set of "bad" characters.
    list_letters_noPunct = [ char for char in raw if char not in exclude ]
    
    # Now we have a list of LETTERS, *join* them back together to get words:
    text_noPunct = "".join(list_letters_noPunct)
    # (http://docs.python.org/3/library/stdtypes.html#str.join)
    
    # Split this big string into a list of words:
    list_words = text_noPunct.strip().split()
    
    # Convert to lower-case letters:
    list_words = [ word.lower() for word in list_words ]

    return list_words


def count_most_common(word_list):
    count_list = list(Counter(word_list).items())
    sort_list = sorted(count_list, key=lambda word: word[1], reverse=True)
    return sort_list

    
words_p = words_of_book('prideandprejudice.txt')
sorted_counts_p = count_most_common(words_p)

words_m = words_of_book('montecristo.txt')
sorted_counts_m = count_most_common(words_m)

w_f_p = list()
for i in sorted_counts_p:
    ind = sorted_counts_p.index(i)
    w_f_p.append([ind+1,i[1]])
    
linear_regressor = LinearRegression()
w_f_pdf = pd.DataFrame(w_f_p, columns=['Log_10(word)','Log_10(frequency)'])
X = w_f_pdf.iloc[:, 0].values.reshape(-1,1)
Y = w_f_pdf.iloc[:, 1].values.reshape(-1,1)
linear_regressor.fit(np.log10(X), np.log10(Y))
print(linear_regressor.coef_)
Y_pred = linear_regressor.predict(np.log10(X))

sns.set_theme()
sns.set_context("paper")

with sns.axes_style("white"):
    sns.despine()
    plot = sns.scatterplot(x='Log_10(word)', y='Log_10(frequency)',
                    alpha=0.5,
                    data=np.log10(w_f_pdf))
    plt.plot(np.log10(X), Y_pred, color='r')
    plt.annotate('rho est = 0.0847', xy=(2.2,3))
    plot.set_title('Pride and Prejudice Rank-Freq')
    
w_f_m = list()
for i in sorted_counts_m:
    ind = sorted_counts_m.index(i)
    w_f_m.append([ind+1,i[1]])
    
w_f_mdf = pd.DataFrame(w_f_m, columns=['Log_10(word)','Log_10(frequency)'])
X = w_f_mdf.iloc[:, 0].values.reshape(-1,1)
Y = w_f_mdf.iloc[:, 1].values.reshape(-1,1)
linear_regressor.fit(np.log10(X), np.log10(Y))
print(linear_regressor.coef_)
Y_pred = linear_regressor.predict(np.log10(X))

sns.set_theme()
sns.set_context("paper")

with sns.axes_style("white"):
    sns.despine()
    plot_m = sns.scatterplot(x='Log_10(word)', y='Log_10(frequency)',
                    alpha=0.5,
                    data=np.log10(w_f_mdf))
    plt.plot(np.log10(X), Y_pred, color='r')
    plt.annotate('rho est = 0.0815', xy=(2.2,3))
    plot_m.set_title('Monte Cristo Rank-Freq')
    
sorted_counts_p[2][1]/len(sorted_counts_p)
sorted_counts_p[3][1]/len(sorted_counts_p)
sorted_counts_m[2][1]/len(sorted_counts_m)
sorted_counts_m[3][1]/len(sorted_counts_m)
