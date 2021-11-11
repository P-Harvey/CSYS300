# Assignment 11

import networkx as nwx
import matplotlib.pyplot as plt
import numpy as np

p = np.geomspace(0.0001,1,num=14)
clust = list()
avg_short = list()
G = nwx.watts_strogatz_graph(1000,10,0,seed=None)
c_null = nwx.average_clustering(G)
a_null = nwx.average_shortest_path_length(G)
for i in list(p):
    G = nwx.watts_strogatz_graph(1000,10,i,seed=None)
    #nwx.draw(G, width=0.15, node_size=5)
    clust.append([i,nwx.average_clustering(G)/c_null])
    avg_short.append([i,nwx.average_shortest_path_length(G)/a_null])
    #plt.show()

a_x = [item[0] for item in avg_short]
a_y = [item[1] for item in avg_short]
c_x = [item[0] for item in clust]
c_y = [item[1] for item in clust]

ax = plt.subplot()
c = plt.plot(c_x,c_y,
             c='black',
             marker='s',
             fillstyle='none',
             linestyle='none')
a = plt.plot(a_x,a_y,
             c='black',
             marker='o',
             linestyle='none')
plt.annotate('C(p)/C(0)', xy=(0.01,0.8))
plt.annotate('L(p)/L(0)', xy=(0.0007,0.2))
plt.xscale('log')
plt.xlabel("p")
plt.show()