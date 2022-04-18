# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit:  <ADD LINK>

+ For the publication page, visit: <ADD LINK>


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


# Data Preprocessing



# Build Docker Images
Snakemake must already be installed. Run `Snakefile` that builds Docker images for each method.


# SK Grid
### Run Model for Predicted Subtypes
Example for running BRCA cohort using BRCA_v12_20210228 as the dataset for predictions
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


# Notes

Most models return the prediction probability for each subtype, where the overall predicted subtype is the one with the highest probability for the given sample. Due to the nature of the machine learning algorithm (ex. SVC, Passive aggressive, SGD, etc.) a few that do not return prediction probabilities will return only the overall predicted subtype.


# Acknowledgment and Funding
We would like to thank the National Cancer Institute for the support.

# Maintainers

Current maintainers:

+ Jordan A. Lee (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
