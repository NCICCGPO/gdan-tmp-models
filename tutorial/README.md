# Tutorial: Breast Cancer Subtype Predictions
## Introduction
For this tutorial, we will be predicting breast invasive carcinoma subtypes using the best gene expression machine learning model from SK Grid. The METABRIC gene expression dataset is freely available to the public at cBioPortal.


## Data Download
Be sure to follow the [README](../README.md) sections `Requirements` and `Setup`.

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


# Build Docker Images
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and SubSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

Here we will build the `SK Grid` method to make predictions on our breast cancer dataset.
```
snakemake --cores 1
```

# Predict Sample Subtypes
Run SK Grid machine learning model on our dataset using `bash RUN_MODEL.sh <method>` where we can use any of the five methods (`skgrid`, `aklimate`, `jadbio`, `cloudforest`, or `subscope`).

Here we will run the `skgrid` method:
```
bash RUN_MODEL.sh skgrid
```

Our molecular matrix with subtype predictions for each sample is located in the method's prediction directory `skgrid/data/preds/`. The columns include sampleID, predicted subtype, and followed by the probability for each cancer cohort subtype. As we can see, the subtype with the highest probability is the predicted subtype in the second column.

|   | Model | Model:Subtype1 | Model:Subtype2 | ... | Model:SubtypeN |
|----|---|---| ---| ---| ---|
| Sample1 | Subtype1 | 0.93 | 0.08 | ... | 0.03 |
| Sample2  | Subtype3 | 0.21 | 0.11 | ... | 0.44
| ...  | ... | ... | ... | ... | ... |
| SampleN | Subtype2 | 0.44 | 0.87 | ... | 0.18 |

Our analysis is now complete!
