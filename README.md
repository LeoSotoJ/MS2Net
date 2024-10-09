# Description

**MNTox** is a Jupyter Notebook pipeline for building spectral networks from MS2 mass spectra and toxicity data and for predicting the Endocrine Disruptive Activity of extracted MS2 features in LC-ESI-HRMS DIA/DDA analysis by-passing feature identification. The MNTox approach has potential for the online or offline screening and prioritization of environmental samples, and for bioactivity screening of small molecules.

The **project page** summarizes the main findings and provides further information with related links on [http://leosotoj.com/pages/project-page](http://leosotoj.com/pages/project-page). 

MNTox is part of a **master thesis** available on [https://uu.diva-portal.org/smash/record.jsf?pid=diva2%3A1875527](https://uu.diva-portal.org/smash/record.jsf?pid=diva2%3A1875527). If you find this project useful you can cite it as shown in the last section.

# Structure and file contents

The contents of this repository are:

- pipeline consisting of 8 directories
- data directory: raw and processed
- scripts directory contaning functions
- settings script to set up the network parameters
- requirements file with the used packages and versions

The pipeline starts with reading the data from an URL or from data/raw. The outputs of each step in the pipeline are stored in data/procesed/. Most of the data files are accompanyied by a Jupyter Notebook that includes a descriptive data analysis in the same subdirectory. 


# Data

## data/raw

	data/raw
	 ├── MassBank
	 │   ├── explore_data.ipynb
	 │   ├── MassBank_NIST.msp
	 │   └── xaf.msp
	 ├── ms2deepscore
	 │   └── MS2DeepScore_allGNPSpositive_10k_500_500_200.hdf5
	 ├── sample
	 │   └── DDA_Pos_EF.csv
	 └── tox21
	     └── tox21_compoundData.csv

File description:

| <div style="width:100px">**Filename**</div> | **Size (MB)** | **Description** | **Source** |
---|---|---|---
`MassBank_NIST.msp` | 90.3 | **MS2 data:** full Mass Bank file from realease version 2022.12.1 | [source](https://github.com/MassBank/MassBank-data/releases/tag/2022.12.1)
`xaf.msp` | 9.03 | **Test file:** sample of the Mass bank with aprox. 10% the size of MassBank_NIST.msp | same as above
`MS2DeepScore_allGNPSpositive_10k_500_500_200.hdf5` | 61.2 | **Trained model:** MS2DeepScore model > 100,000 MS/MS spectra GNPS (Huber,2021) | [source](https://zenodo.org/records/4699356)
`DDA_Pos_EF.csv`  | <1 | **Sample data:** internal laboratory data of environmental sample in DDA mode, extracted MS2 features | internal lab data
`tox21_compoundData.csv` | 1.4 | **Toxicity data:** InChIKeys and Endpoints activity from tox21 challenge in tabular format | [source](http://bioinf.jku.at/research/DeepTox/tox21_compoundData.csv)

## data/processed

	data/processed
	 ├── CosineSimilarity
	 │   ├── 01b_exploring_cosine_values.ipynb
	 │   ├── MassBank_NIST_Feb20_cosine_tol0.1.csv
	 │   └── xaf_cosine_tol0.01.csv
	 ├── MolecularNetwork
	 │   ├── MassBank_NIST_Feb20_MS2DeepScore_cutoff0.7_links10.graphml
	 │   └── MassBank_NIST_Feb20_tol0.1_cutoff0.6_links10.graphml
	 ├── ms2deepscore
	 │   ├── MassBank_NIST_Feb20_ms2deepscore.csv
	 │   └── xaf_ms2deepscore.csv
	 ├── MS2MassBank
	 │   ├── explore_data_processed.ipynb
	 │   ├── MassBank_NIST_Feb20_metadata.msp
	 │   ├── ... 
	 │   ├── metrics_cosine.csv
	 │   ├── xaf_metadata.msp
	 │   └── ...
	 ├── MS2_tox
	 │   ├── 2023_05_07_intensity_matrix_endpoints.csv
	 │   └── ...
	 └── tox21
	     ├── explore_dataset.ipynb
	     └── tox.csv

File description:

| <div style="width:100px">**Filename**</div> | **Description** |
---|---
`01b_exploring_cosine_values.ipynb` | notebook with exploratory analysis of cosine values
`MassBank_NIST_Feb20_cosine_tol0.1.csv` | cosine values for a tolerance of 0.1 m/z
`xaf_cosine_tol0.01.csv` | result obtained with the test file xaf.msp
`MassBank_NIST_Feb20_MS2DeepScore_cutoff0.7_links10.graphml` | network file obtained from the MS2DeepScore similarities
`MassBank_NIST_Feb20_tol0.1_cutoff0.6_links10.graphml` | network file obtained from the cosine similarities
`MassBank_NIST_Feb20_ms2deepscore.csv` | MS2DeepScore similarity scores
`xaf_ms2deepscore.csv` | MS2DeepScores for the test file
`explore_data_processed.ipynb` | descriptive analysis of MS2 data
`MassBank_NIST_Feb20_metadata.msp` | intermediate results of processing MS2 spectra
`metrics_cosine.csv` | results with the selected model
`xaf_metadata.msp` | intermediate results with the test file
`2023_05_07_intensity_matrix_endpoints.csv` | table with MS2 and toxicity data combined on the first run
`explore_dataset.ipynb` | exploratory analysis of the tox21 file
`tox.csv` | processed tox21 file

<br>

# BibTeX
If you find this project useful, you can cite it as:

  <div class="container">
    <pre><code>@masterthesis{Soto_2023,
  title={Automated Prediction of the Endocrine Disruptive Potency of Chemicals detected with LC/ESI/HRMS based on Mass Spectral Networks},
  url={https://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-532906},
  author={Soto, Leonardo},
  year={2023},
  collection={UPKEM E}
}</code></pre>
  </div>


