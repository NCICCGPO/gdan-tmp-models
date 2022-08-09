# Introduction
A collection of machine learning models that make predictions of cancer molecular subtypes. Users can run predictions on their molecular data. Data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

These tools were created from the GDAN-TMP group where minimal molecular markers were used to accurately predict 26 different cancer cohorts and 106 subtypes. Of the 1000's of models ran, the models with high predictive accuracy are made available to the public here.

+ For the publication of this work, visit:  <ADD LINK>

+ For the publication page, visit: <ADD LINK>

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


# Data Requirements
User input data must be in tab separated format.

# 1. Pre-processing User Data
Input data **must have proper feature labeling and rescaling prior** to running machine learning models for subtype predictions.

### 1A. Feature Relabeling and Transposing
First, machine learning models need to be able to match genes to GDAN-TMP specific gene IDs (ex. convert gene TP53 to feature N:GEXP::TP53:7157:). Then reformatting to a sample x feature matrix.
```
python tools/convert.py \
	--data <original-user-data> \
	--out <relabeled-user-data> \
	--cancer <cancer>
```

### 1B. Quantile Rescaling
Second, relabeled data must be transformed with a quantile rescale prior to running machine learning algorithms. The rescaled output file will always be located in `user-transformed-data/transformed-data.tsv`.
```
bash tools/run_transform.sh \
  <relabeled-user-data>
```

# 2. Download Method Models
Certain methods require large or source files to run models. These files are available for download from the Publication page or through Synapse directly.

> Required step: download associated model data for certain methods

**CloudForest download** of model data: download from the *publication page* `models_cf.tar.gz` (SynapseID syn31752640) into the directory `cloudforest/data/` and decompress.

**JADBio download** of model data: download from the *publication page* `models_jadbio.tar.gz` (SynapseID syn31110725) into the directory `jadbio/data/` and decompress.

```
# In the data dir - Decompress
tar -xvf <file.tar.gz>
```

SK Grid, AKLIMATE, and subSCOPE do not need manual model data download.

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
+ Model options: `CNVR, GEXP, METH, MIR, MUTA`
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
