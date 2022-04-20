# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit:  <ADD LINK>

+ For the publication page, visit: <ADD LINK>

Subtype predictions can be made for the following [TCGA cohorts](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations):

`ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM`

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


# Build Docker Images
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and SubSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

Build Docker images of these methods from `Snakefile`.
```
snakemake --cores 1
```


# SK Grid
### Run Model for Predicted Subtypes
Most models return the prediction probability for each subtype, where the overall predicted subtype is the one with the highest probability for the given sample. Due to the nature of the machine learning algorithm (ex. SVC, Passive aggressive, SGD, etc.) a few that do not return prediction probabilities will return only the overall predicted subtype.
```
cd skgrid
bash RUN.sh
```


# AKLIMATE
Allowed platform types: TOP, MULTI, GEXP, CNVR, or METH
No models for MIR or MUTA for any cancer cohorts. No models for ACC GEXP, BRCA METH, OV MULTI, PAAD GEXP, SKCM CNVR, or UVM GEXP.

### Run Model for Predicted Subtypes
```
cd aklimate
bash RUN.sh
```


# SubSCOPE
### Run Model for Predicted Subtypes
```
cd subscope
bash RUN.sh
```
There are several files on the details for the predictions. The best subtype predictions are included in `subscope/data/preds/<platfrom>-subscope-results.txt`.


# JADBio
### Run Model for Predicted Subtypes
```
cd jadbio
bash RUN.sh
```


# Cloud Forest ML
### Prep
Input feature matrices and a predictor forest must be already created.

Feature matrices must be placed in `cloudforest/CF_For_Docker/KIRCKICH/FM/` with the format:
| .  | tes3 | tes6 | ... |
|----|---|---| ---|
| B:0 | 1 | 1 | ... |
| feature1  | 0.037816 | 0.056716 | ... |
| feature2  | 0.059439 | 0.088822 | ... |
| ... | ... | ... | ... |

Predictor forests must be placed in `cloudforest/CF_For_Docker/KIRCKICH/SF/`

Output folder for predictions should already exist `cloudforest/CF_For_Docker/KIRCKICH/CL/`


### Run Model For Predicted Subtypes
Cloud forest machine learning model can be ran as a CWL workflow. Run ML and saves predictions in `CL/`
```
cd cloud-forest/
bash RUN.sh
```
Where the output predictions are saved as a tsv with non-named columns that are `[CaseLabel, Predicted, Actual]`

# Tutorial
An example of how to run the prediction workflow is shown [here](tutorial/README.md) using SK Grid best performing gene expression model on a breast cacner cBioPortal dataset.

# Acknowledgment and Funding
We would like to thank the National Cancer Institute for the support.

# Maintainers

Current maintainers:

+ Jordan A. Lee (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
