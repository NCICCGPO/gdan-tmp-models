# Tutorial: Breast Cancer Subtype Predictions
## Introduction
For this tutorial, we will be predicting breast invasive carcinoma subtypes using the best gene expression machine learning model from SK Grid. The METABRIC gene expression dataset is freely available to the public at cBioPortal.

> Here we will build the `SK Grid` method to make predictions on our breast cancer dataset.

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
First, machine learning models need to be able to match genes to GDAN-TMP specific gene IDs. We will convert `brca_metabric/data_mrna_agilent_microarray.txt` Entrez gene IDs and reformat into a sample x feature matrix (ex. convert gene TP53 to feature N:GEXP::TP53:7157:). The output file can be found at `user-transformed-data/cbioportal_BRCA_GEXP.tsv`.
```
# Rename and format data_mrna_agilent_microarray.txt
python tools/convert.py \
	--data brca_metabric/data_mrna_agilent_microarray.txt \
	--out user-transformed-data/cbioportal_BRCA_GEXP.tsv \
	--cancer BRCA
```

Second, data must be transformed with a quantile rescale prior to running machine learning algorithms. The output file can be found at `user-transformed-data/transformed-data.tsv`
```
# Quantile Rescale
bash tools/run_transform.sh \
  user-transformed-data/cbioportal_BRCA_GEXP.tsv
```


# Platform Options
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and SubSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

Note: there are some exceptions, see section "Additional Info: Model Selection and Input Specifications" in [README.md](../README.md) for details.

# Predict Sample Subtypes
We can pick from any of the five methods `SK Grid`, `AKLIMATE`, `JADBio`, `CloudForest`, or `SubSCOPE`. We also will want to pick which of the 6 models we want to use to make our subtype predictions (see the six models listed in Tutorial section "Platform Options").

To run any model, execute `bash RUN_MODEL.sh <cancer> <platform> <method> <user-data>`. We will run the full pipeline to make predictions for our dataset using SK Grid's best GEXP only model (model that was trained using the TCGA BRCA cancer cohort as its training data).
```
bash RUN_MODEL.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv
```

The above line will 1) generate the CWL input file and 2) run the machine learning model inside a Docker container using CWL.

Our molecular matrix with subtype predictions for each sample is located in the method's prediction directory `skgrid/data/preds/`. The columns include sampleID, predicted subtype, and followed by the probability for each cancer cohort subtype. As we can see, the subtype with the highest probability is the predicted subtype in the second column.

|   | Model | Model:Subtype1 | Model:Subtype2 | ... | Model:SubtypeN |
|----|---|---| ---| ---| ---|
| Sample1 | Subtype1 | 0.93 | 0.08 | ... | 0.03 |
| Sample2  | Subtype3 | 0.21 | 0.11 | ... | 0.44
| ...  | ... | ... | ... | ... | ... |
| SampleN | Subtype2 | 0.44 | 0.87 | ... | 0.18 |

**Our analysis is now complete!**

All five methods (SK Grid, AKLIMATE, CloudForest, SubSCOPE, and JADBio) are ran the same way. However, the output format of the prediction file(s) is specific to each method - view each method's README.md for details.


# Understanding RUN_MODEL.sh
The **first step** called by `RUN_MODEL.sh` is to automatically generate the CWL input file and can be viewed in `user-job-ymls/`. This file will tell the method how to run.

Below is the content of `user-job-ymls/skgrid-inputs.yml` where we want to predict subtypes on our data "transformed-data.tsv" using the breast cancer model for gene expression only and the output file will have the prefix BRCA_GEXP_skgrid.
```
cancer:
  - BRCA
platform:
  - GEXP
input_data:
  - class: File
    path: ../user-transformed-data/transformed-data.tsv
output_prefix:
  - BRCA_GEXP_skgrid
```

The **second step** called by `RUN_MODEL.sh` will run the machine learning model. Models are will make sample level subtype predictions for our dataset. This is ran in a Docker container that is created by a CWL workflow. Certain methods have multiple steps (executed as tools), for instance SK Grid will generate a large library of different machine learning models, train models using TCGA data then save trained models as pickles, and predict subtypes for each sample in our dataset.
