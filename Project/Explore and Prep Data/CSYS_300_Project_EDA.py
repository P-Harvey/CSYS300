# CSYS 300 Working Project (Python Version)
# PATRICK HARVEY

from matplotlib import pyplot as plt
from plasm import chasm                                                        # Courtesy Prof. James 'Jim' Bagrow
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os, sys, getpass, pickle, copy

def read_in(f):                                                                # Read the FEA data in to pandas dataframe
        path = os.getcwd()
        try:
            in_file = path + '\\Data\\'  + f
        except FileNotFoundError:
            path = '/Users/Harvey/Library/Mobile Documents/com~apple~CloudDocs/CSYS300/Project/Data/'
            in_file = path + f
        data = pd.read_csv(in_file)
        return data

def compare_var(s, d):                                                         # Create comparables for each variable
    return d.loc[d['Variable_Code'] == s]                                      # In reality, separating the observations
                                                                               # by the variable being observed.
def comparables(d):                                                            # Put all of the variables in to a dictionary
    variable = d.loc[:,'Variable_Code'].unique()                               # Will take ~20 sec on first run
    compare_dict = {}                                                          # but can repeatedly call user_in
    for i in variable:                                                         # in console to compare different variables
        compare_dict[i] = compare_var(i, d)
    return compare_dict

def user_in(c_d):                                                              # Function to run iteratively to compare
    data_1 = input('Data 1: ')                                                 # different variables
    V = c_d[data_1].loc[:,'Value']
    data_2 = input('Data 2: ')
    W = c_d[data_2].loc[:,'Value']
    data_3 = input('Data 3: ')
    X = c_d[data_3].loc[:,'Value']
    data_4 = input('Data 4: ')
    Y = c_d[data_4].loc[:,'Value']
    data_5 = input('Data 5: ')
    Z = c_d[data_5].loc[:,'Value']
    names = [data_1, data_2, data_3, data_4, data_5]
    chasm(V, W, X, Y, Z, names=names, show_median=True)

def start_here(c_d):
    data_1 = input('Data 1: ')                                                 # different variables
    V = c_d[data_1].loc[:,'Value']
    data_2 = input('Data 2: ')
    W = c_d[data_2].loc[:,'Value']
    X = c_d['PCT_WICINFANTCHILD14'].loc[:,'Value']
    Y = c_d['PCT_OBESE_ADULTS12'].loc[:,'Value']
    Z = c_d['PCT_HSPA17'].loc[:,'Value']
    names = [data_1, data_2, 'PCT_WICINFANTCHILD14',
             'PCT_OBESE_ADULTS12', 'PCT_HSPA17']
    chasm(V, W, X, Y, Z, names=names, show_median=True)
    
def check_depend(c_d):
    data_1 = input('Data 1: ')                                                 # different variables
    V = c_d[data_1].loc[:,'Value']
    data_2 = input('Data 2: ')
    W = c_d[data_2].loc[:,'Value']
    plot_out(V, W)
    lin_fit_plot(V, W)
    
def plot_out(x, y):
    x1 = list(range(0,len(x)))
    y1 = list(range(0,len(y)))
    fig, ax = plt.subplots()
    ax.plot(sorted(x), x1)
    ax.plot(sorted(y), y1)
    plt.xscale('log')
    plt.yscale('log')
    ax.grid(True)
    plt.show()
    
def lin_fit_plot(x, y):
    x = np.array(sorted(np.log10(x))).reshape((-1,1))
    x1 = np.array(list(range(0,len(np.log10(x))))).reshape((-1,1))
    model = LinearRegression().fit(x1,x)
    r_sq = model.score(x1, x)
    print('Coefficient of Determination: ',r_sq)
    print('Intercept: ',model.intercept_)
    print('Slope: ', model.coef_)
    x_pred = model.predict(x1)
    plt.scatter(x1,x)
    plt.plot(x1,x_pred)
    plt.xscale('log')
    plt.show()
    
def gen_compare_plots(v_d, user_input):
    if user_input == "1":
        user_in(v_d)
    elif user_input == "2":
        check_depend(v_d)
    else:
        user_input = input("Incorrect input. Please enter 1, 2, or q to quit: ")
        if user_input.lower() == 'q':
            return
        else:
            gen_compare_plots(v_d, user_input)

def package_data(v_d):
    v_d_c = copy.deepcopy(v_d)
    pickle.dump(v_d_c, open('FEA_data.pkl', 'wb'))
    return


filename = 'StateAndCountyData.csv'
FEA_data = read_in(filename)
var_dict = comparables(FEA_data)
user = input("Enter 1 to select 5 variables, or 2 to select 2 variables: ")
gen_compare_plots(var_dict, user)
package_data(var_dict)
sys.exit("Goodbye {}!".format(getpass.getuser()))