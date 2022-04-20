# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit:  <ADD LINK>

+ For the publication page, visit: <ADD LINK>

Subtype predictions can be made for the following [TCGA cohorts](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations):

`ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM`

### Model Library Available
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and SubSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features


# Requirements
The following are required:

+ Python 3+ https://www.python.org/downloads/
+ Docker or Docker Desktop https://www.docker.com/
+ cwl-runner https://github.com/common-workflow-language/cwltool
+ Synapse client https://help.synapse.org/docs/Installing-Synapse-API-Clients.1985249668.html and create an account
+ AWS https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
+ Snakemake https://snakemake.readthedocs.io/en/stable/getting_started/installation.html


# Setup
Create an environment and install dependencies
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.text
```

Setup for Synapse and AWS
```
synapse login --remember-me
```
And create `~/.aws/credentials`
```
[default]
aws_access_key_id=XXX
aws_secret_access_key=XXX
```


# Data Requirements
User input data must be in tab separated format.


# Analyze: Run Machine Learning Models to Predict Cancer Subtypes
Simple command to call one of the five methods. This will predict the molecular subtype for each sample.
```
bash RUN_MODEL.sh <method-name>
```
Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

For example, to run the SK Grid method use `bash RUN_MODEL.sh skgrid`.


# Tutorial
An example of how to run the prediction workflow is shown [here](tutorial/README.md) using SK Grid best performing gene expression model on a breast cacner cBioPortal dataset.


# Acknowledgment and Funding
We would like to thank the National Cancer Institute for the support.


# Maintainers
Current maintainers:

+ Jordan A. Lee (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
