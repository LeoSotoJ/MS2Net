#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append('../')

import pandas as pd
import numpy as np

from settings import MSrawdata
from scripts.standarise_data import count_spectrums
from matchms.importing import load_from_msp


# ## MassBank.eu Mass Spectra

# Imported from https://github.com/MassBank/MassBank-data/releases/tag/2022.12.1 Release version 2022.12.1 | MassBank_NIST.msp 90.3 MB, Feb 20.
# 
# matchms v. 0.18.0 is used for processing the metadata, peaks, and spectral networking. https://github.com/matchms/matchms

# In[2]:


print('MS dataset: ', MSrawdata)


# In[4]:


data_path = '../data/processed/MS2MassBank/'


# In[6]:


spectrums=[]
spectrums = list(load_from_msp('../data/raw/MassBank/'+MSrawdata+'.msp'))


# In[4]:


count_spectrums(spectrums)


# ### Metadata Processing

# Repair InchiKeys from other information (e.g., SMILES)

# In[5]:


import matchms.filtering as ms_filters
def metadata_processing(spectrum):
    spectrum = ms_filters.default_filters(spectrum)
    spectrum = ms_filters.repair_inchi_inchikey_smiles(spectrum)
    spectrum = ms_filters.derive_inchi_from_smiles(spectrum)
    spectrum = ms_filters.derive_smiles_from_inchi(spectrum)
    spectrum = ms_filters.derive_inchikey_from_inchi(spectrum)
    spectrum = ms_filters.harmonize_undefined_smiles(spectrum)
    spectrum = ms_filters.harmonize_undefined_inchi(spectrum)
    spectrum = ms_filters.harmonize_undefined_inchikey(spectrum)
    spectrum = ms_filters.add_precursor_mz(spectrum)
    return spectrum


# In[6]:


spectrums = [metadata_processing(s) for s in spectrums]


# In[8]:


from matchms.exporting import save_as_msp
save_as_msp(spectrums, data_path+MSrawdata+'_metadata.msp')


# In[ ]:


#from matchms.importing import load_from_msp
#spectrums = []
#spectrums = list(load_from_msp(data_path+MSrawdata+'_metadata.msp'))


# In[9]:


count_spectrums(spectrums)


# ### Tox21 InchiKeys filter

# In[10]:


tox=pd.read_csv('../data/processed/tox21/tox.csv')
tox.set_index('inchikey', inplace=True)
inchikeys_tox21=tox.index.tolist()


# In[11]:


spectrums = [s for s in spectrums 
          if s.metadata.get('inchikey') in inchikeys_tox21
          and s.metadata.get('ionmode') == 'positive'
          and s.metadata.get('adduct') == '[M+H]+'
          and s.metadata.get('ms_level') == 'MS2' 
          and 'LC-ESI' in s.metadata.get('instrument_type')
                ]


# In[12]:


count_spectrums(spectrums)


# In[13]:


from matchms.exporting import save_as_msp
save_as_msp(spectrums, data_path+MSrawdata+'_metadata_toxfilter.msp')


# ### Peaks processing

# In[14]:


import matchms.filtering as ms_filters


# In[15]:


import matchms.filtering as ms_filters
def peak_processing(spectrum):
    spectrum = ms_filters.default_filters(spectrum)
    spectrum = ms_filters.normalize_intensities(spectrum)
    spectrum = ms_filters.select_by_intensity(spectrum, intensity_from=0.05)
    return spectrum
spectrums = [peak_processing(s) for s in spectrums]


# In[16]:


save_as_msp(spectrums, data_path+MSrawdata+'_metadata_toxfilter_peak.msp')

