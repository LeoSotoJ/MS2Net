#!/usr/bin/env python
# coding: utf-8

# Spectrums with the same inchikey are combined into one spectrum that contains all the peaks

# In[1]:


import sys
sys.path.append('../')

import pandas as pd
import numpy as np

from collections import Counter, defaultdict
from scripts.standarise_data import count_spectrums
from settings import MSrawdata

from matchms.importing import load_from_msp
from matchms import Spectrum

data_path = '../data/processed/MS2MassBank/'

# In[2]:


print('MS dataset: ', MSrawdata)


# In[2]:


spectrums=[]
spectrums = list(load_from_msp(data_path+MSrawdata+"_metadata_toxfilter_peak.msp"))


# In[3]:


count_spectrums(spectrums)


# In[4]:


#Frequency of spectrums by inchikey
inchikeys=[s.get('inchikey') for s in spectrums]
frequency_counter = Counter(inchikeys)
inchikey = list(frequency_counter.keys())
frequency = list(frequency_counter.values())
df = pd.DataFrame.from_dict(frequency_counter, orient='index', columns=['Frequency'])
df.index.name = 'inchikey'
df.to_csv(data_path+'frequency_inchikeys_before_merging.csv')
df


# In[5]:


# Creating a dictionary to group spectrums by their inchikey
spectrums_by_inchikey = defaultdict(list)
for s in spectrums:
    inchikey = s.get('inchikey')
    spectrums_by_inchikey[inchikey].append(s)
spectrums_by_inchikey


# In[6]:


# Adding all spectrums to a combined spectrum per each inchikey
combined_spectrums = []
for inchikey, spectra in spectrums_by_inchikey.items():
    mz_data = np.concatenate([s.mz for s in spectra])
    intensity_data = np.concatenate([s.intensities for s in spectra])

    sort_indices = np.argsort(mz_data)
    mz_data_sorted = mz_data[sort_indices]
    intensity_data_sorted = intensity_data[sort_indices]

    combined_spectrum = Spectrum(mz=mz_data_sorted,
                                 intensities=intensity_data_sorted,
                                 metadata={'inchikey': inchikey})
    combined_spectrums.append(combined_spectrum)


# In[7]:


from matchms.exporting import save_as_msp
save_as_msp(combined_spectrums, data_path + MSrawdata + '_metadata_toxfilter_peak_combined.msp')


# In[8]:


#Total peaks by combined spectrum
inchikey_combined = [s.get('inchikey') for s in combined_spectrums]
peaks=[len(s.peaks.mz) for s in combined_spectrums]
df_peaks = pd.DataFrame({'num_peaks':peaks},index=inchikey_combined)
df_peaks.index.name = 'inchikey'
df_peaks.to_csv(data_path+'len_peaks_after_merging.csv')
df_peaks


# In[ ]:




