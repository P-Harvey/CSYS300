# PATRICK L HARVEY
# plharvey@uvm.edu
# CSYS-300 Fall 2021
# Assignment 6

import numpy as np
import matplotlib as mp
import pandas as pd
import random
import time
from collections import Counter

class Elephant:
    def __init__(self, flavor, rho):
        self.flavor = flavor
        self.rho = rho
    def getFlavor(self):
        return self.flavor
    def getRho(self):
        return self.rho
    
def run_rho(e_rho, e_list):
    if len(e_list) == 1:
        hmm = np.random.random()
        if hmm > e_rho:
            e_list.append(Elephant(e_list[0].flavor, e_rho))
        else:
            e_list.append(Elephant(e_list[0].flavor+1, e_rho))
    else:
        k = list(Counter(Elephant.flavor for Elephant in e_list).items())
            
            
            
            
    
    
    
    e_list.append[E]
    if hmm > E_list[0].rho:
        E_list.append(Elephant(E_list[0].flavor, E_list[0].rho))
    else:
        E_list.append(Elephant(E_list[0].flavor+1, E_list[0].rho))
        
    for i in range(1, size, 1):
        hmm = np.random.random()
        repl_prob = 1-(E_list[i].getRho())
        ele_flav = E_list[i].getFlavor()
        tmp = list(Counter(Elephant.flavor for Elephant in E_list).items())
        num_ele_k = tmp[ele_flav-1][1]
        t = len(E_list)
        replicate_k = repl_prob*num_ele_k/t
        if hmm > replicate_k:
            E_list.append(Elephant(E_list[i].flavor, E_list[i].rho))
        else:
            E_list.append(Elephant(E_list[i].flavor+1, E_list[i].rho))
    k = list(Counter(Elephant.flavor for Elephant in E_list).items())
    k_x = [e[0] for e in k]
    k_y = [e[1] for e in k]
    mp.pyplot.scatter(k_x, k_y)
    mp.pyplot.xlabel('Flavor (N_k)')
    mp.pyplot.ylabel('Quantity (kN_k)')
    mp.pyplot.xscale('log')
    mp.pyplot.yscale('log')
    mp.pyplot.show()

E = Elephant(1, 0.1)
E_list = [E]

run_rho(0.1, 19999)
run_rho(0.01, 19999)
run_rho(0.001, 19999)