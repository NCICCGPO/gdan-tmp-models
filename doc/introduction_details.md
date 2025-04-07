# About the Tumor Molecular Pathology Toolkit (TMP toolkit)

A collection of machine learning models that make predictions of cancer molecular subtypes. Users can predict cancer subtypes on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

> Users can run the TMP toolkit on their datasets to determine the cancer subtypes present

## Data Availability and Publication

Visit Cancer Cell for the publication of this work (open access): 

+ [Classification of non-TCGA cancer samples to TCGA molecular subtypes using compact feature sets](https://doi.org/10.1016/j.ccell.2024.12.002)

Data are freely available for download:

+ [Publication Page](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022)

    > Note: Data required to run tool must be downloaded from here

## A Tool for Many Cancer Cohorts

The TMP toolkit is applicable to 26 different cancer cohorts (ex. breast invasive carcinoma, colon adenocarcinoma) and has been trained on TCGA primary tumor samples to assign any of 106 cancer subtype to new samples.  

Subtype predictions can be made for the following:

ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM

> Full cancer cohort names of these abbreviations can be [found here](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations)

## Leaverage a Large Library of Pre-Trained Models

The TMP toolkit was derived from the best of tens to thousands of models. The top performing pre-trained models have been made available in Docker containers.

Specifically, there are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and subSCOPE). The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. `OVERALL` model - highest performing model
2. `GEXP` only model - highest performing model using only gene expression features
3. `CNVR` only model - highest performing model using only copy number features
4. `MUTA` only model - highest performing model using only mutation features
5. `METH` only model - highest performing model using only DNA methylation features
6. `MIR` only model - highest performing model using only miRNA features

There are a few **exceptions** to models provided by certain methods, see **"Additional Info: Model Selection and Input Specifications"** section below.

Docker images for each model are pulled automatically in workflow shown in the "Analyze" section below. Docker images are stored in:

+ [CCG_TMP_Public Synapse Space](https://www.synapse.org/#!Synapse:syn29568296/docker/).

## Details of All Pre-Trained Models
We have made publicly available the top models (above section) and any new data can get subtype predictions from these models. Explore these well-performing models by seeing the algorithm name, parameters, and required feature list. The feature lists will be returned in TMP nomenclature.

Example of model information. For more details see: [Explore_models.md](tutorial/Explore_models.md)
```
{'model': 'sklearn.ensemble.RandomForestClassifier',
 'model_params': {'criterion': 'entropy', 'n_estimators': 200},
 'fts': ['N:GEXP::CENPA:1058:',
  'N:GEXP::FOXC1:2296:',
  'N:GEXP::ESR1:2099:',
  'N:GEXP::MBOAT1:154141:',
  'N:GEXP::MIA:8190:',
  'N:GEXP::ANXA3:306:',
  'N:GEXP::WDR67:93594:',
  'N:GEXP::NAT1:9:',
  'N:GEXP::EXO1:9156:']}
```