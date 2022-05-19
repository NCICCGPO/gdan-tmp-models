# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit:  <ADD LINK>

+ For the publication page, visit: <ADD LINK>

Subtype predictions can be made for the following [TCGA cohorts](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations):

> ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM`

### Model Library Available
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and SubSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

There are a few **exceptions** to models provided by certain methods, see **"Model Selection and Input Specifications"** section below.

Docker images for each model are pulled automatically in workflow shown in the "Analyze" section below. Docker images are stored in [CCG_TMP_Public Synapse Space](https://www.synapse.org/#!Synapse:syn29568296/docker/).

# Requirements
The following are required:

+ Python 3+ https://www.python.org/downloads/
+ Docker or Docker Desktop https://www.docker.com/
+ cwl-runner https://github.com/common-workflow-language/cwltool
+ Synapse client https://help.synapse.org/docs/Installing-Synapse-API-Clients.1985249668.html and create an account
+ AWS https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


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

# Download Method Model Data
Certain methods require large files to run models. These files are available for download from the Publication page or through Synapse directly.

> Required step: download associated model data for certain methods

**CloudForest download** of model data: download data.tar.gz (`syn30564146`) into the directory `cloudforest/`, and decompress.


# Model Selection and Input Specifications
Edit the file in `user-job-ymls/` that is associated with the method.

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

Each method file is slightly different, but all will require selection of at least the input dataset, cancer model, and data platform. Available values are noted in each method's yaml file.

Model platform name differs for each method, see below:

+ SK Grid options: `OVERALL, CNVR, GEXP, METH, MIR, or MUTA` where OVERALL is the highest performing model regardless of platform (can be single data platform type or a combination).

+ AKLIMATE options: `TOP, GEXP, CNVR, METH, or MULTI` where TOP is the highest performing model regardless of platform (can be single data platform type or a combination). MULTI is a combination of multiple data platform types.

+ CloudForest options: `OVERALL, MULTI, CNVR, GEXP, METH, MIR, or MUTA` where `OVERALL` is the best model for the cancer cohort. `MULTI` stands for using all available data types. **Not all cancer cohorts have a MULTI model** this only occurs if it is the highest performing model (of all models) is a non-single data platform model.

+ SubSCOPE options: `CNV, GEXP, METH, MIR, MUTA`. Note this method **requires** the use of `CNV` not CNVR.

+ JADBio options:

# Analyze: Run Machine Learning Models to Predict Cancer Subtypes
Simple command to call one of the five methods. This will predict the molecular subtype for each sample `bash RUN_MODEL.sh <arguments>`

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

Specifically:
```
bash RUN_model.sh <cancer> <platform> <method> <your-data>
```

Examples for BRCA cancer cohorts are:
+ bash RUN_model.sh BRCA GEXP cloudforest user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA TOP aklimate user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP subscope user-transformed-data/transformed-data.tsv


# Tutorial
An example of how to run the prediction workflow is shown [here](tutorial/README.md) using SK Grid best performing gene expression model on a breast cancer cBioPortal dataset.

# Alternative Image Pull
Docker images for methods are automatically pulled and built by CWL workflows and tools from the public Synapse repository. Alternatively, Docker images can be manually pulled and built using:
```
synapse get <synapse-ID>
docker load -i <image.tar.gz>
```

| SynapseID | Name |
|----|---|
| syn29658355  | sk_grid.tar.gz |
| syn29659459  | aklimate.tar.gz |
| syn30267068  | cloudforest.tar.gz |
| SYNID  | JADBIOIMAGE |
| syn26284209 | dockerimage-subscope-ccg-tmp.tar.gz |


# Acknowledgment and Funding
We would like to thank the National Cancer Institute for the support.


# Maintainers
Current maintainers:

+ Jordan A. Lee (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
