# Tutorial: Breast Cancer Subtype Predictions
## Introduction
For this tutorial, we will be predicting breast invasive carcinoma subtypes using the best gene expression machine learning model from SK Grid. The METABRIC gene expression dataset is freely available to the public at cBioPortal.

## Data Download
Be sure to follow the README sections `Requirements` and `Setup`.

This step requires `wget` to be installed already.
```
# Download Gene Expression Data
wget  https://cbioportal-datahub.s3.amazonaws.com/brca_metabric.tar.gz
tar -xf brca_metabric.tar.gz brca_metabric/data_mrna_agilent_microarray.txt
rm brca_metabric.tar.gz
```

We will be predicting subtypes for `data_mrna_agilent_microarray.txt`.

## Pre-Processing
First, machine learning models need to be able to match genes to GDAN-TMP specific gene IDs. We will convert from Entrez gene IDs and reformat into a sample x feature matrix. The output file can be found at `user-transformed-data/cbioportal_BRCA_GEXP.tsv`.
```
# Rename and format data_mrna_agilent_microarray.txt
python tools/convert.py
```

Second, data must be transformed with a quantile rescale prior to running machine learning algorithms. The output file can be found at `user-transformed-data/transformed-data.tsv`
```
# Quantile Rescale
bash run_transform.sh user-transformed-data/cbioportal_BRCA_GEXP.tsv
```
