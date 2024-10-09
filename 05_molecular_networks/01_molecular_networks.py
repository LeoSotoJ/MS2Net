#!/usr/bin/env python
# coding: utf-8

# In[4]:

import sys
sys.path.append('../')
from settings import MSrawdata


# In[ ]:


#receiving var from py script
scores = sys.argv[1]


# In[5]:


print('MS dataset: ', MSrawdata)


# In[6]:


data_path_net = '../data/processed/MolecularNetwork/'
cosine_tolerance=0.1
cutoff=0.7
links=10


# In[7]:


import networkx as nx
import matchmsextras.networking as net
from matchms.networking import SimilarityNetwork
network = SimilarityNetwork(identifier_key="inchikey",
                               score_cutoff=cutoff,
                               max_links=links,
                              keep_unconnected_nodes=False)
network.create_network(scores,  score_name="CosineGreedy_score")
#network = network.graph


# In[78]:


nx.write_graphml(network, data_path_net + MSrawdata+"_tol"+str(cosine_tolerance)+"_cutoff"+str(cutoff)+"_links"+str(links)+".graphml")


# In[79]:


net.plot_cluster(network)

