# Patrick Harvey
# CSYS 300 Assignment 8
# Fall 2021

import math
import statistics as stats
from matplotlib import pyplot as plt
from itertools import islice
import copy

p = list(range (0,101,1))
L = {20:{}, 50:{}, 100:{}, 200:{}, 500:{}, 1000:{}}
data = {}
for j in p:
    j = j/100
    data[j] = copy.deepcopy(L)

keys = list(data.keys())
sub_keys = list(data[0.01].keys())
Occ = dict()


for k in keys:
    for s in sub_keys:
        L = copy.deepcopy(L)
        l = s
        p = k
        F_p = p**4 + 4*((p**3)*(1-p)) +4*(p**2*(1-p)**2)
        lst = list()
        for i in range(s):
            lst.append([F_p, F_p*i])
        L[s] = lst
    data[k] = copy.deepcopy(L)


for s in sub_keys:
    x, y, z = list(), list(), list()
    for k in keys:
        y1 = data[k]
        y1 = y1[s]
        for i in y1:
            y2 = i[1]
            y.append(y2)
        x.append(k)
        y_max = max(y)
        y_mean = y_max/s
        z.append(y_mean)
    line_1 = plt.plot(x,z, label = 'S_avg')
    line_2 = plt.plot(x,x, label = 'F(p) = p')
    plt.title(label='L='+str(s))
    plt.xlabel(xlabel='p')
    plt.ylabel(ylabel='Length of Run / L')
    plt.legend()
    #plt.xscale('log')
    #plt.yscale('log')
    plt.show()
    
p = [0.39, 0.39/2, 0.39+(1-0.39)/2]
#p = [0.39]
L = 10000
for i in p:
    x_list = list()
    y_list = list()
    for l in range(L):
        y = i**4 + 4*((i**3)*(1-i)) +4*(i**2*(1-i)**2)
        y = i**l*(1-i)**2
        try:
            y_list.append(y*l)
        except ZeroDivisionError:
            y_list.append(0)
        x_list.append(l)
    plt.plot(x_list,y_list, label ='{:.3f}'.format(i))
    #plt.plot(x_list,x_list, label = 'F(p) = p')
plt.title(label='L='+str(L))
plt.xlabel(xlabel='n_l')
plt.ylabel(ylabel='Count of n_l')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.show()
