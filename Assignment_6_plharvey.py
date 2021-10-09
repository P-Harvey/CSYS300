# PATRICK L HARVEY
# plharvey@uvm.edu
# CSYS-300 Fall 2021
# Assignment 6

import numpy as np
import pandas as pd
import seaborn as sns
from collections import Counter
from matplotlib import pyplot as plt
from scipy import special as sp
from sklearn.linear_model import LinearRegression

n = 10000
rho = 0.1
a = list(range(1,n))
b = (2-rho)/(1-rho)
n_k = list()
for i in a:
    first = (1-rho)**(i+1)
    second = sp.beta(a[i-1],b)
    n_k.append([i, first*second])
    
n_k_2 = list()
for i in a:
    first = i
    second = -(2-rho)/(1-rho)
    n_k_2.append([i, first**second])

n_k_2df = pd.DataFrame(n_k_2, columns=['Log_10(k)','Log_10(n_k)'])


n_k_df = pd.DataFrame(n_k, columns=['Log_10(k)','Log_10(n_k)'])
X = n_k_2df.iloc[:, 0].values.reshape(-1,1)
Y = n_k_2df.iloc[:, 1].values.reshape(-1,1)
linear_regressor = LinearRegression()
linear_regressor.fit(np.log10(X), np.log10(Y))
print(linear_regressor.coef_)
Y_pred = linear_regressor.predict(np.log10(X))

sns.set_theme()
sns.set_context("paper")

with sns.axes_style("white"):
    sns.despine()
    plot = sns.scatterplot(x='Log_10(k)', y='Log_10(n_k)',
                    alpha=0.5,
                    data=np.log10(n_k_df))
    plt.plot(np.log10(X), Y_pred, color='r')
    plt.annotate('alpha = -1.001001', xy=(2,-2))
    plot.set_title('Rho = 0.01; t=10,000')

##############################################################################
word_frequency = {}
with open('ulysses.txt') as f:
    for line in f:
        split_line = line.split(':')
        word_frequency[split_line[0]] = int(split_line[1])

frequency = list()
word = list()
for k in word_frequency.keys():
    word.append(k)
    frequency.append(word_frequency[k])


x_list = list(range(1,len(frequency)+1))
counted = sorted(list(Counter(frequency).items()))

w_f = list()
for i in counted:
    w_f.append([i[0],i[1]])

w_f_df = pd.DataFrame(w_f, columns=['Log_10(word)','Log_10(frequency)'])
X = w_f_df.iloc[:101, 0].values.reshape(-1,1)
Y = w_f_df.iloc[:101, 1].values.reshape(-1,1)
linear_regressor.fit(np.log10(X), np.log10(Y))
print(linear_regressor.coef_)
Y_pred = linear_regressor.predict(np.log10(X))

sns.set_theme()
sns.set_context("paper")

with sns.axes_style("white"):
    sns.despine()
    plot = sns.scatterplot(x='Log_10(word)', y='Log_10(frequency)',
                    alpha=0.5,
                    data=np.log10(w_f_df))
    plt.plot(np.log10(X), Y_pred, color='r')
    plt.annotate('rho est = 0.0102', xy=(2.2,3))
    plot.set_title('Ulysses Rank-Freq')
    
w_f_z = zip(x_list, sorted(frequency, reverse=True))
w_f_2df = pd.DataFrame(w_f_z, columns=['Log_10(word)','Log_10(frequency)'])
X = w_f_2df.iloc[:, 0].values.reshape(-1,1)
Y = w_f_2df.iloc[:, 1].values.reshape(-1,1)
linear_regressor.fit(np.log10(X), np.log10(Y))
print(linear_regressor.coef_)
Y_pred = linear_regressor.predict(np.log10(X))

sns.set_theme()
sns.set_context("paper")

with sns.axes_style("white"):
    sns.despine()
    plot = sns.scatterplot(x='Log_10(word)', y='Log_10(frequency)',
                    alpha=0.5,
                    data=np.log10(w_f_2df))
    plt.plot(np.log10(X), Y_pred, color='r')
    plt.annotate('rho est = 0.0123', xy=(2.2,3))
    plot.set_title('Ulysses Rank-Freq')
    
counted[2][1]/len(frequency)
counted[3][1]/len(frequency)



