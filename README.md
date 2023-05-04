# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit: (TBA until after manuscript publication)

+ For the publication page, visit: (TBA until after manuscript publication)

> Model data downloads from publication page are required to run certain models

Subtype predictions can be made for the following [TCGA cohorts](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations):

> ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM

### Model Library Available
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and subSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

There are a few **exceptions** to models provided by certain methods, see **"Additional Info: Model Selection and Input Specifications"** section below.

Docker images for each model are pulled automatically in workflow shown in the "Analyze" section below. Docker images are stored in [CCG_TMP_Public Synapse Space](https://www.synapse.org/#!Synapse:syn29568296/docker/).

### Which Machine Learning Models
We have made publicly available the top models (above section) and any new data can get subtype predictions from these models. Explore these well performing models by seeing the algorithm name, parameters, and required feature list. The feature lists will be returned in TMP nomenclature.

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

# Requirements
The following are required:

+ Python 3+ https://www.python.org/downloads/
+ Docker or Docker Desktop https://www.docker.com/
+ Synapse client https://help.synapse.org/docs/Installing-Synapse-API-Clients.1985249668.html and create an account
+ AWS https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


# Setup
1. Create an environment and install dependencies. This will install cwlref-runner version 1.0, this version is required to run analysis.
```
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

2. Synapse Sign In
```
synapse login --remember-me
```

3. Docker Sign In (if not already)
```
docker login
```

4. Synapse Docker Registry Sign In - using Syanpse username and password
```
docker login -u <synapse-username> docker.synapse.org
```


# 1. Download Data (Method Models and Feature Renaming Reference Files)
### 1A. Reference files for transform (project matrices)
Download and decompress the reference files that are used as the target data space for data transformations (ex. quantile rescaling).

The `TMP_20230209.tar.gz` file (SynapseID syn51081157) can be downloaded from the Publication Page and then placed in `tools/`
```
cd tools
tar -xzf TMP_20230209.tar.gz
cd ..
```

### 1B. Method Models
Certain methods require large or source files to run models. These files are available for download from the Publication page or through Synapse directly.

> Required step: download associated model data for certain methods

**CloudForest download** of model data: download from the *publication page* `models_cf.tar.gz` (SynapseID syn31752640) into the directory `cloudforest/data/` and decompress.

**JADBio download** of model data: download from the *publication page* `models_jadbio.tar.gz` (SynapseID syn31110725) into the directory `jadbio/data/` and decompress.

**SK Grid download** of model data: copy over this file from tools
```
cp -r tools/TMP_20230209 skgrid/data/src/training_data/
```

AKLIMATE and subSCOPE do not need manual model data download.

### 1C. Feature Renaming Reference Files
Download and decompress the reference files - renaming any user data feature to nomenclature that machine learning models will recognize (TMP nomenclature).

The `ft_name_convert.tar.gz` file (SynapseID syn51315102) can be downloaded from the Publication Page and then placed in `tools/`
```
cd tools
tar -xzf ft_name_convert.tar.gz
cd ..
```


# Data Requirements
User input data must be in tab separated format.

# 2. Pre-processing User Data
Input data **must have proper feature labeling and rescaling prior** to running machine learning models for subtype predictions.

### 2A. Feature Relabeling and Transposing
First, machine learning models need to be able to match genes to GDAN-TMP specific gene IDs (ex. convert gene TP53 to feature N:GEXP::TP53:7157:). Then reformatting to a sample x feature matrix.
```
python tools/convert.py \
	--data <original-user-data> \
	--out <relabeled-user-data> \
	--cancer <cancer>
```
An optional argument of `--delete_i_col` can be included. An optional argument to inform which column to remove (0 based indexing). Use if a meta-data column is in data. If not specified, then will run with no column deletions.

### 2B. Quantile Rescaling
Second, relabeled data must be transformed with a quantile rescale prior to running machine learning algorithms. The rescaled output file will always be located in `user-transformed-data/transformed-data.tsv`.
```
bash tools/run_transform.sh \
  <relabeled-user-data> \
	<cancer>
```

# 3. Run Machine Learning Models to Predict Cancer Subtypes
Simple command to call one of the five methods. This will predict the molecular subtype for each sample `bash RUN_MODEL.sh <arguments>`

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

Specifically:
```
bash RUN_model.sh <cancer> <platform> <method> <your-data>
```

Examples for BRCA cancer cohorts are:
+ bash RUN_model.sh BRCA GEXP cloudforest user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP aklimate user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP jadbio user-transformed-data/transformed-data.tsv
+ bash RUN_MODEL.sh BRCA GEXP subscope user-transformed-data/transformed-data.tsv


# Tutorial
An example of how to run the prediction workflow is shown [here](tutorial/README.md) using SK Grid best performing gene expression model on a breast cancer cBioPortal dataset.

# Alternative Model Download (Optional)
Docker images for methods are automatically pulled and built by CWL workflows and tools from the public Synapse repository.

Alternatively:
1. Docker images can be manually downloaded by going to the publication page for each method image file.
```
# ImageFiles
sk_grid.tar.gz
aklimate.tar.gz
cloudforest.tar.gz
jadbio.tar.gz
subscope.tar.gz
```

2. Build each method's docker image.
```
docker load -i <imagefile.tar.gz>
```
Check these images have been successfully loaded with `docker images`.

Note that some methods have an additional model data file to run. These can be found at the publication page (see section Download Method Model Data)


# Additional Info: Model Selection and Input Specifications
Each the file in `user-job-ymls/` is associated with the method and is automatically generated from `RUN_MODEL.sh`.

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

Each method file is slightly different, but all will require selection of at least the input dataset, cancer model, and data platform. Available values are noted in [tools/options.yml](tools/options.yml).

Model platform name differs for each method, see below:

### SK Grid options
+ Model options: `OVERALL, CNVR, GEXP, METH, MIR, or MUTA` where OVERALL is the highest performing model regardless of platform (can be single data platform type or a combination).
+ Additional method details found in [SK Grid README](skgrid/README.md)

### AKLIMATE options
+ Model options: `TOP, GEXP, CNVR, METH, or MULTI` where TOP is the highest performing model regardless of platform (can be single data platform type or a combination). MULTI is a combination of multiple data platform types.
+ Additional method details found in [AKLIMATE README](aklimate/README.md)

### CloudForest options
+ Model options: `OVERALL, MULTI, CNVR, GEXP, METH, MIR, or MUTA` where `OVERALL` is the best model for the cancer cohort. `MULTI` stands for using all available data types. **Not all cancer cohorts have a MULTI model** this only occurs if it is the highest performing model (of all models) is a non-single data platform model.
+ Additional method details found in [CloudForest README](cloudforest/README.md)

### subSCOPE options
+ Model options: `allcohorts, CNVR, GEXP, METH, MIR, MUTA` where `allcohorts` is the best model when trained with all cohorts simultaneously and will return the best subtype predictions regardless of cohort (ex. a users dataset can be returned with a mixture of subtypes from breast and liver cancers).
+ Additional method details found in [subSCOPE README](subscope/README.md)

### JADBio options
+ Model options: `MULTI, CNVR, GEXP, METH, MIR, MUTA` where `MULTI` stands for using all available data types.
+ Additional method details found in [JADBio README](jadbio/README.md)


# Acknowledgment and Funding
We would like to thank the National Cancer Institute for the support.

# Troubleshooting
See [How to Fix Common Issues](tutorial/error_messages.md) for common error messages.

# Maintainers
Current maintainers:

+ Jordan A. Lee (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
+ Brian Karlberg (GitHub briankarlberg)
