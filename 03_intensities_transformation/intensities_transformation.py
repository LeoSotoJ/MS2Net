#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append('../')

import pandas as pd
import numpy as np

from scripts.standarise_data import count_spectrums
from settings import MSrawdata
from matchms.importing import load_from_msp

data_path = '../data/processed/MS2MassBank/'


# In[ ]:


print('MS dataset: ', MSrawdata)


# In[2]:


spectrums=[]
spectrums = list(load_from_msp(data_path+MSrawdata+"_metadata_toxfilter_peak_combined.msp"))


# In[3]:


count_spectrums(spectrums)


# In[4]:


import math
import copy
from matchms import Spectrum

transformed_spectrums = []
for spectrum in spectrums:
    transformed_intensities = np.sqrt(spectrum.intensities)  
    transformed_spectrum = Spectrum(mz=spectrum.mz, intensities=transformed_intensities, metadata=spectrum.metadata)
    transformed_spectrums.append(transformed_spectrum)


# In[5]:


from matchms.exporting import save_as_msp
save_as_msp(transformed_spectrums, data_path + MSrawdata + '_transformed.msp')

