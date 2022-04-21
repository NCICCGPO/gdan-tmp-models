# Tutorial: Breast Cancer Subtype Predictions
## Introduction
For this tutorial, we will be predicting breast invasive carcinoma subtypes using the best gene expression machine learning model from SK Grid. The METABRIC gene expression dataset is freely available to the public at cBioPortal.

Here we will build the `SK Grid` method to make predictions on our breast cancer dataset.

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


# Predict Sample Subtypes
We can pick from any of the five methods `SK Grid`, `AKLIMATE`, `JADBio`, `CloudForest`, or `SubSCOPE`. We also will want to pick which of the 6 model we want to use to make our subtype predictions (see the six models listed in Tutorial section "Build Docker Images").

We will prepare for running SK Grid by editing job input file associated with the method that is in `user-job-ymls/`. This file will tell the method how to run. Below is the content of `user-job-ymls/skgrid-inputs.yml` where we want to predict subtypes on our data "transformed-data.tsv" using the breast cancer model for gene expression only and the output file will have the prefix BRCA_GEXP.
```
## Select one or more for each section ##


# User Data to Predict Subtypes (ex. transformed-data.tsv)
input_data:
  - class: File
    path: ../user-transformed-data/transformed-data.tsv

# TCGA Cancer cohort
cancer:
  - "BRCA"

# Data Platform (SK Grid top model)
# Options: OVERALL, CNVR, GEXP, METH, MIR, MUTA
platform:
  - "GEXP"

# Subtype Prediction File Prefix
# Options: BRCA_OVERALL, BRCA_CNVR, BRCA_GEXP, BRCA_METH, BRCA_MIR, BRCA_MUTA
output_prefix:
  - "BRCA_GEXP"
```

Now we are ready to run the model. Run SK Grid machine learning model on our dataset using `bash RUN_MODEL.sh <method>` where we can use any of the five methods (`skgrid`, `aklimate`, `jadbio`, `cloudforest`, or `subscope`) - note all are a single lowercase name.

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
