# Setup

Create environment and setup
```
python -m venv venv
. venv/bin/activate
```

Install `cwl-runner` and `Docker`


Synapse and AWS
```
synapse login --remember-me
```

create `~/.aws/credentials`

```
[default]
aws_access_key_id=XXX
aws_secret_access_key=XXX
```

# Build Docker Images
Snakemake must already be installed. Run `Snakefile` that builds Docker images for each method.


# AKLIMATE
### Build image with permissions updated
```
cd aklimate
docker build --tag aklimate2 .
```
### Run Model for Predicted Subtypes
```
# Predict subtypes
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


# SK Grid
### Run Model for Predicted Subtypes
Example for running BRCA cohort using BRCA_v12_20210228 as the dataset for predictions
```
cd skgrid
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
