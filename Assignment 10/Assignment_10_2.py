# Patrick Harvey
# CSYS-300 Fall 2021
# Assignment 10

import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import measurements
from matplotlib import colors

"""
Yield = p - <l>
p = density (total trees/total area)
<l> = average loss in density computed over P(i,j)
"""

def new_forest(L, D):
    check_ind = dict()
    f_f = range(0,L**2)
    forest_fraction = [i/L**2 for i in f_f]
    P = prob_fire(L)
    F = np.zeros((L, L))
    m_F = np.zeros((L,L))
    yield_l = list()
    for i in forest_fraction:
        fsd = list()
        for d in range(D):
            Dx = np.random.randint(L)
            Dy = np.random.randint(L)
            check_ind[d] = (Dx,Dy)
        k_l = check_ind.keys()
        for k in k_l:
            coord = check_ind[k]
            S, p, ar = forest_size(F, coord, P)
            fsd.append(S*p)
        tt = np.where(F==1)
        tt = F[tt].sum()/(L**2)
        pp = perc_prob(L, F, P)
        fsd = fsd.index(min(fsd))
        yield_l.append(tt - pp)
        if (tt-pp) >= 0.5234375:
            m_F = copy.deepcopy(F)
            m_y = max(yield_l)
            z_s = sorted(copy.deepcopy(ar), reverse=True)
        F[check_ind[fsd]] = 1
    to_plot(m_F,D,L,m_y)
    zipf_plot_s(z_s,D,L,m_y)
    return F, yield_l

def zipf_forest(L, D):
    check_ind = dict()
    f_f = range(0,L**2)
    forest_fraction = [i/L**2 for i in f_f]
    P = prob_fire(L)
    z_list = np.arange(0.1,1,0.1)
    F = np.zeros((L, L))
    yield_l = list()
    for i in forest_fraction:
        fsd = list()
        for d in range(D):
            Dx = np.random.randint(L)
            Dy = np.random.randint(L)
            check_ind[d] = (Dx,Dy)
        k_l = check_ind.keys()
        for k in k_l:
            coord = check_ind[k]
            S, p, ar = forest_size(F, coord, P)
            fsd.append(S*p)
        tt = np.where(F==1)
        tt = F[tt].sum()/(L**2)
        pp = perc_prob(L, F, P)
        fsd = fsd.index(min(fsd))
        yield_l.append(tt - pp)
        if round(tt, 2) in z_list:
            m_y = max(yield_l)
            z_p = sorted(copy.deepcopy(ar), reverse=True)
            zipf_plot_p(z_p,D,L,m_y)
        F[check_ind[fsd]] = 1

def perc_prob(L, F, Pr):
    for ip in range(L):
        m = F==1
        lw, num = measurements.label(m)
        perc_x = np.intersect1d(lw[0,:],lw[-1,:])
        perc = perc_x[np.where(perc_x>0)]
        if (len(perc)>0):
            area = measurements.sum(m, lw, perc[0])
        else:
            area = 0
    return area/(L**2)

def prob_fire(L):
    p_32 = dict()
    for i in range(L):
        row = list()
        for j in range(L):
            e_i = np.exp(-i/l[0])
            e_j = np.exp(-j/l[0])
            row.append(e_i*e_j)
        p_32[i] = row
    f = pd.DataFrame.from_dict(p_32)
    column_maxes = f.max()
    df_max = column_maxes.max()
    normalized_df = f/df_max
    norm = np.linalg.norm(normalized_df)
    f = normalized_df/norm
    return f.to_numpy()

def forest_size(F, xy, P):
    m = F==1
    lw, num = measurements.label(m)
    labelList = np.arange(lw.max() + 1)
    area = measurements.sum(m, lw, labelList)
    size_c = lw[xy]
    pcoord = np.where(lw==size_c)
    sum_p = P[pcoord].sum()
    size = area[size_c]
    return size, sum_p, area

def to_plot(arr,d,l,my):
    # Colors for visualization: white for tree, black for firebreak
    colors_list = [(0,0,0), (1,1,1), (1,1,1)]
    cmap = colors.ListedColormap(colors_list)
    bounds = [0,1,2,3]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    fig = plt.figure(figsize=(25/3, 6.25))
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(arr, cmap=cmap, norm=norm)
    plt.title("Peak Yield for D={} {}x{}".format(d,l,l))
    plt.annotate("Peak@{:.4f}".format(my), (l/2,0), c='red', 
                 backgroundcolor='white')
    plt.show()
    
def zipf_plot_p(ZP, D, L, my):
    plt.plot(ZP) # Plot Zipf and annotate
    plt.title("Zipf Cluster Size at dens={:.2f} {}x{}".format(my,L,L))
    plt.annotate("Dens: {:.2f}".format(my), (1, 1), 
                 c='red', backgroundcolor='white')
    plt.ylabel("Cluster Size")
    plt.xlabel("Rank")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
def zipf_plot_s(ZS, D, L, my):
    plt.plot(ZS) # Plot Zipf and annotate
    plt.title("Zipf For Max Yield Cluster Size at D={} {}x{}".format(D,L,L))
    plt.annotate("Peak: {:.4f}".format(my), (1, 1), 
                 c='red', backgroundcolor='white')
    plt.ylabel("Cluster Size")
    plt.xlabel("Rank")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

length = 1 # Choose L index
decis = 6 # Choose D index

L = [32,64,128] # Parameters for lattice size
D = [1,2,3,L[0],L[0]**2,L[1],L[1]**2,L[2],L[2]**2] # Parameters for decision space
l = [i/10 for i in L] # Given scaling factor
F, yld = new_forest(L[length], D[decis]) # Generate a forest
zipf_forest(L[length], D[decis])

x_pos = yld.index(max(yld)) # Get index of max yield

plt.plot(yld) # Plot yield and annotate
plt.title("Yield v. Tree Count for D={} {}x{}".format(D[decis],
                                                      L[length],L[length]))
plt.annotate("Peak: {:.4f}".format(max(yld)), 
              (x_pos-150, 0), 
              c='red', backgroundcolor='white')
plt.ylabel("Yield")
plt.xlabel("Trees Added")
plt.show()