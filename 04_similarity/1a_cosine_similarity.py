#!/usr/bin/env python
# coding: utf-8

# In[18]:

import sys
sys.path.append('../')

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

from datetime import datetime, date, time
from scripts.standarise_data import count_spectrums
from matchms.importing import load_from_msp
from settings import MSrawdata

cosine_tolerance=0.1
data_path = '../data/processed/MS2MassBank/'
data_path_sim = '../data/processed/CosineSimilarity/'


# In[ ]:


print('MS dataset: ', MSrawdata)


# In[3]:


spectrums=[]
spectrums = list(load_from_msp(data_path+MSrawdata+"_transformed.msp"))


# In[4]:


len(spectrums)


# In[5]:


#Calculate cosine scores using the CosineGreedy function.
#Two peaks are matched if their m/z ratios lie in a certain tolerance

from matchms import calculate_scores
from matchms.similarity import CosineGreedy

similarity_measure = CosineGreedy(tolerance=cosine_tolerance)
print('Start: ' + datetime.now().strftime('%H:%M:%S'))
scores = calculate_scores(spectrums, spectrums, similarity_measure, is_symmetric=True)
print('End: ' + datetime.now().strftime('%H:%M:%S'))


# In[6]:


#%store scores


# In[29]:


#scores.scores.data["CosineGreedy_score"]


# In[7]:


scores_array = scores.scores.to_array()
scores_array.tofile(data_path_sim+'cosine_scores_'+MSrawdata+'.csv', sep = ';')


# In[21]:


inchikeys = [s.metadata['inchikey'] for s in spectrums]
scores_df = pd.DataFrame(scores_array["CosineGreedy_score"], index=inchikeys, columns=inchikeys)
#matches_df=pd.DataFrame(scores_array["CosineGreedy_matches"], index=inchikeys, columns=inchikeys)
scores_df.to_csv(data_path_sim + MSrawdata +"_cosine_tol"+str(cosine_tolerance)+".csv")


# In[40]:


min_match = 3
plt.figure(figsize=(6,6), dpi=150)
plt.imshow(scores_array[:10,:10]["CosineGreedy_score"] \
           * (scores_array[:10,:10]["CosineGreedy_matches"] >= min_match), cmap="viridis")
plt.colorbar(shrink=0.7)
plt.title("Cosine_score spectra similarities (min_match=3)")
plt.xlabel("Spectrum #ID")
plt.ylabel("Spectrum #ID")


# In[ ]:


# Pass scores variable to the network script

import subprocess
subprocess.Popen(["python", "../05_molecular_networks/01_molecular_networks.py", scores]).wait()

#import 05_molecular_networks.01_molecular_networks
#exec(open("../05_molecular_networks/01_molecular_networks.py").read())

#import subprocess
#subprocess.Popen(f"python ../05_molecular_networks/01_molecular_networks.py {scores}", shell=True)

#subprocess.Popen("../05_molecular_networks/01_molecular_networks.py scores", shell=True)
#os.system("../05_molecular_networks/01_molecular_networks.py scores")
#subprocess.run(["python3", "../05_molecular_networks/01_molecular_networks.py", scores])


