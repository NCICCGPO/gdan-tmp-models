<h1 align="center">Tumor Molecular Pathology Toolkit</h1>
<h4 align="center">An easy-to-run tool to classify cancer samples to defined TCGA subtypes using molecular profile data</h4>


## Table of contents

- [Introduction](#introduction)
- [Data Availability and Publication](#data-availability-and-publication)
- [Quickstart Guide](#quickstart-guide)
- [Tutorials](#tutorials)
- [Acknowledgment and Funding](#acknowledgment-and-funding)
- [Troubleshooting](#troubleshooting)
- [Maintainers](#maintainers)


## Introduction
The TMP toolkit is designed to classify cancer samples to subtypes using molecular data. This tool can provide reliable subtype classification on non-TCGA studies, clinical trials, or other user datasets.

The top-performing models (of the hundreds of thousands models evaluated) have been pre-trained and available within Docker containers for ease of use.

The TMP toolkit is applicable to 26 different cancer cohorts (ex. breast invasive carcinoma, colon adenocarcinoma) and has been trained on TCGA primary tumor samples to classify any of 106 cancer subtype to new samples.  


Cancer cohorts include:

+ ACC, BLCA, BRCA, CESC, COADREAD, ESCC, GEA, HNSC, KIRCKICH, KIRP, LGGGBM, LIHCCHOL, LUAD, LUSC, MESO, OV, PAAD, PCPG, PRAD, SARC, SKCM, TGCT, THCA, THYM, UCEC, UVM

  > Full cancer cohort names of these abbreviations can be [found here](https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/tcga-study-abbreviations). Note that our study combined several of the TCGA primary tumors in the linked list


The data platforms supported are gene expression, DNA methylation, miRNA, copy number, and/or mutation calls.

## Data Availability and Publication

Visit Cancer Cell for the publication of this work (open access): 

+ [Classification of non-TCGA cancer samples to TCGA molecular subtypes using compact feature sets](https://doi.org/10.1016/j.ccell.2024.12.002)

Data are freely available for download:

+ [Publication Page](https://gdc.cancer.gov/about-data/publications/CCG-TMP-2022)

    > Note: Data required to run tool must be downloaded from the above link

## Quickstart Guide

### Setup

Install requirements - detailed instructions are found on the [Requirements page](doc/requirements.md):

1. Install Python 3+
2. Install Docker Desktop (or Docker)
3. Install Synapse Client
4. Install AWS Client

Ensure that steps are completed on the [Requirements page](doc/requirements.md) - *(includes creating working environment, signining in, and manually downloading required data)*

> Alternatively, Docker images can be built directly. Instructions are found on the [Requirements page](doc.requirements.md)

### Required Input Format
Activate the python virtual environment 
```bash
source venv/bin/activate
```

User input data must be in tab-separated format (.tsv) - where original user data has rows labeled with samples and columns labeled with features (ex. genes).

> Ensure your data matches above description

### Update Feature Nomenclature

Translate your feature names (ex. genes, etc.) from Entrez IDs to our unique TMP tooklit IDs and transpose matrix.

> Example: convert gene TP53 to feature N:GEXP::TP53:7157:

```bash
python tools/convert.py \
	--data <path/to/my-data.tsv> \
	--out <path/to/my-updated-data.tsv> \
	--cancer <cancer>
```

If the data contains a meta-data column, use the option argument `--delete_i_col` to delete the specified column (where *n* is an integer with zero-based indexing). If not specified, then will run with no column deletions.

### Quantile Rescaling

Next, data must be transformed with a quantile rescale prior to running machine learning algorithms. 

```bash
# Transform - creates transformed-data.tsv
bash tools/run_transform.sh \
  <path/to/my-updated-data.tsv> \
	<cancer>

python tools/zero_floor.py \
  -in user-transformed-data/transformed-data.tsv \
  -out user-transformed-data/transformed-data.tsv
```

> The rescaled output file will written to disk at `user-transformed-data/transformed-data.tsv`.

### Run Machine Learning Models to Predict Cancer Subtypes

Run a single command to predict the molecular subtype all samples.

```
bash RUN_model.sh <cancer> <platform> <method> <user-transformed-data/transformed-data.tsv>
```

> Available cancers: `ACC`, `BLCA`, `BRCA`, `CESC`, `COADREAD`, `ESCC`, `GEA`, `HNSC`, `KIRCKICH`, `KIRP`, `LGGGBM`, `LIHCCHOL`, `LUAD`, `LUSC`, `MESO`, `OV`, `PAAD`, `PCPG`, `PRAD`, `SARC`, `SKCM`, `TGCT`, `THCA`, `THYM`, `UCEC`, `UVM` 

> Available platforms: `GEXP`, `METH`, `MUTA`, `MIR`, `CNVR` 
> - ([see model details](doc/model_details.md) for `OVERALL`, `TOP`, `MULTI`, `All`, `allcohorts`)

> Available methods: `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`


*Examples:*

+ *Run the SK Grid model that was trained on gene expression for the breast invasive carcinoma cohort*

  ```bash RUN_model.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv```


+ *Run the AKLIMATE model that was trained on DNA methylation for the pancreatic adenocarcinoma cohort*

  ```bash RUN_model.sh PAAD METH aklimate user-transformed-data/transformed-data.tsv```


+ *Run the CloudForest model that was trained on somatic mutations for the colon adenocarcinoma + rectum adenocarcinoma combined cohort*

  ```bash RUN_model.sh COADREAD MUTA cloudforest user-transformed-data/transformed-data.tsv```

## Tutorials

For a guided tutorial of running our models for subtype classification, see the [Guided Tutorial](doc/tutorial/walk_thru_tutorial.md) page.

To understand the specific parameters and other details of individual containerized models, see the [Explore Models](doc/tutorial/Explore_models.md) page.

To interprete and convert the TMP Toolkit subtype abbreviations, see the [Understanding Subtype Abbreviations](doc/tutorial/Explore_cancer_subtypes.md) page. 


  + > Our models use the BRCA_1 abbreviation to denote the luminal A subtype. Learn how to automatically convert TMP Toolkit abbreviations to common names for all our subtypes

## Troubleshooting
See [How to Fix Common Issues](doc/error_messages.md) for common error messages.

## Acknowledgment and Funding
We would like to thank the National Cancer Institute for support.

## Maintainers
Current maintainers:

+ Jordan Tagle (GitHub jordan2lee)
+ Kyle Ellrott (GitHub kellrott)
+ Brian Karlberg (GitHub briankarlberg)
