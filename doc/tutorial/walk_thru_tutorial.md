# Guided Tutorial

Obtaining Breast Cancer Subtype Predictions

## Introduction
For this tutorial, we will be predicting breast invasive carcinoma subtypes using the best gene expression machine learning model from SK Grid. The METABRIC gene expression dataset is freely available to the public at cBioPortal.

> Here we will build the `SK Grid` method to make predictions on the breast cancer dataset.

## 1. Data Download
Be sure to follow the [README](../README.md) sections `Requirements` and `Setup`.

This step requires `wget` to be installed already.
```
# Download Gene Expression Data
wget  https://cbioportal-datahub.s3.amazonaws.com/brca_metabric.tar.gz
tar -xf brca_metabric.tar.gz brca_metabric/data_mrna_illumina_microarray.txt
rm brca_metabric.tar.gz
```

We will be predicting subtypes for `data_mrna_illumina_microarray.txt`.


## 2. Pre-Processing
Run the sub-step that corresponds to the data type of the input dataset. If following tutorial with the METABRIC data, then follow the gene expression sub-step.

### 2.1 Convert Feature Nomenclature of METABRIC data and Reformat Matrix
Machine learning models need to be able to match genes to GDAN-TMP specific gene IDs. We will convert `brca_metabric/data_mrna_illumina_microarray.txt` Entrez gene IDs and reformat into a sample x feature matrix (ex. convert gene TP53 to feature N:GEXP::TP53:7157:). The output file can be found at `user-transformed-data/cbioportal_BRCA_GEXP.tsv`.


Rename and format data_mrna_illumina_microarray.txt
```
python tools/convert.py \
	--data brca_metabric/data_mrna_illumina_microarray.txt \
	--out user-transformed-data/cbioportal_BRCA_GEXP.tsv \
	--cancer BRCA \
	--conversion_file tools/ft_name_convert/entrez2tmp_BRCA_GEXP.json \
	--delete_i_col 1
```
> this last line is dataset specific. 0 based index

Note that the `--delete_i_col` is an optional argument to inform which column to remove (in this case the METABRIC data has a metadata column at index 1 so we will delete this by specifying 1 as the value of `--delete_i_col`).

### **How to Convert Data into the Correct Feature Nomenclature (Manual)**
The above section details how to convert features to the nomenclature machine models will recognize (TMP nomenclature) specifically for METABRIC data. Use this section to convert any data to TMP nomenclature.

**A. Gene Expression Data Example for Three Features (Entrez gene IDs):**
+ First use `tools_ml()`:
```
import sys
sys.path.append('tools/')
import tools_ml
```
```
# Create a list of data gene symbols
# Example:
user_entrez = ['155060', '100130426','10357']

# Specify cancer cohort
cancer = 'BRCA'
```
```
# Use GEXP converter to get ordered list of TMP Feature IDs
tools_ml.gexp_converter(user_entrez, cancer)
```
+ Next replace these TMP feature IDs with those in the data. Then dedup the data so that there aren't multiple columns that have the same TMP feature ID. If there are multiple columns with the same TMP feature ID then randomly select one to keep because the TMP Toolkit models found that these features exist in the same cytoband and have similar molecular profiles.

+ Next remove any columns with the string name `nan`. These are features not used by machine learning models and therefore aren't need to receive predictions

+ Finally, make sure the data matrix is formatted where the rows are samples and columns are features


**B. Copy Number Variation Data Example for Three Features (gene symbols):**
The input data must have the features be gene symbols for using the conversion tool to map it to its corresponding GDAN-TMP feature id.

+ First, use `tools_ml()`:
```
import sys
sys.path.append('tools/')
import tools_ml
```
```
# Create a list of data gene symbols
# Example:
user_CNVR_symbols = ['ATAD3C', 'LINC01128','PLEKHG5']

# Specify cancer cohort
cancer = 'BRCA'
```
```
# Use CNVR converter to get ordered list of TMP Feature IDs
tools_ml.cnvr_converter(user_CNVR_symbols, cancer)
```

+ Next replace these TMP feature IDs with those in the data. Then dedup the data so that there aren't multiple columns that have the same TMP feature ID. If there are multiple columns with the same TMP feature ID then randomly select one to keep because the TMP Toolkit models found that these features exist in the same cytoband and have similar molecular profiles.

+ Finally, make sure the data matrix is formatted where the rows are samples and columns are features

### 2.2 Rescale Data into ML Data Space
Data must be transformed with a quantile rescale prior to running machine learning algorithms. The output file can be found at `user-transformed-data/transformed-data.tsv`
```
# Quantile Rescale
bash tools/run_transform.sh \
  user-transformed-data/cbioportal_BRCA_GEXP.tsv \
	BRCA

# Handle 10 quantile differences
python tools/zero_floor.py \
  -in user-transformed-data/transformed-data.tsv \
  -out user-transformed-data/transformed-data.tsv
```


## 3. Understanding Platform Options
There are five methods (SK Grid, AKLIMATE, CloudForst, JADBio, and subSCOPE) and each ran tens to thousands of models. The top performing models of each method, for each of the 26 cancer cohorts have been made available, and include:

1. Best `OVERALL` model - highest performing model
2. Best `GEXP` only model - highest performing model using only gene expression features
3. Best `CNVR` only model - highest performing model using only copy number features
4. Best `MUTA` only model - highest performing model using only mutation features
5. Best `METH` only model - highest performing model using only DNA methylation features
6. Best `MIR` only model - highest performing model using only miRNA features

Note: there are some exceptions, see section "Additional Info: Model Selection and Input Specifications" in [README.md](../README.md) for details.

## 4. Predicting Sample Subtypes
Simple command to call one of the five methods. We also will want to pick which of the 6 models we want to use to make the subtype predictions (see the six models listed in Tutorial section "Platform Options").

> Available methods are `skgrid`, `aklimate`, `cloudforest`, `jadbio`, and `subscope`.

To run any model, execute `bash RUN_MODEL.sh <cancer> <platform> <method> <user-data>`. We will run the full pipeline to make predictions for the dataset using SK Grid's best GEXP only model (model that was trained using the TCGA BRCA cancer cohort as its training data).
```
bash RUN_MODEL.sh BRCA GEXP skgrid user-transformed-data/transformed-data.tsv
```

The above line will 1) generate the CWL input file and 2) run the machine learning model inside a Docker container using CWL.

The molecular matrix with subtype predictions for each sample is located in the method's prediction directory `skgrid/data/preds/`. The columns include sampleID, predicted subtype, and followed by the probability for each cancer cohort subtype. As we can see, the subtype with the highest probability is the predicted subtype in the second column.

|   | Model | Model:Subtype1 | Model:Subtype2 | ... | Model:SubtypeN |
|----|---|---| ---| ---| ---|
| Sample1 | Subtype1 | 0.93 | 0.08 | ... | 0.03 |
| Sample2  | Subtype3 | 0.21 | 0.11 | ... | 0.44
| ...  | ... | ... | ... | ... | ... |
| SampleN | Subtype2 | 0.44 | 0.87 | ... | 0.18 |

### Understanding RUN_MODEL.sh
The **first step** called by `RUN_MODEL.sh` is to automatically generate the CWL input file and can be viewed in `user-job-ymls/`. This file will tell the method how to run.

Below is the content of `user-job-ymls/skgrid-inputs.yml` where we want to predict subtypes on the data "transformed-data.tsv" using the breast cancer model for gene expression only and the output file will have the prefix BRCA_GEXP_skgrid.
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

The **second step** called by `RUN_MODEL.sh` will run the machine learning model. Models are will make sample level subtype predictions for the dataset. This is ran in a Docker container that is created by a CWL workflow. Certain methods have multiple steps (executed as tools), for instance SK Grid will generate a large library of different machine learning models, train models using TCGA data then save trained models as pickles, and predict subtypes for each sample in the dataset.

## 5. Generate Summary File of Prediction Results
All five methods (SK Grid, AKLIMATE, CloudForest, subSCOPE, and JADBio) are ran the same way. However, the output format of the prediction file(s) is specific to each method - view each method's README.md for details. Here we will take care of that and generate a single file with the results of all methods.

First let's move the results into a working directory called `results_dir` or any name. We also specify the cancer cohort and data platform we ran the machine learning models on.
```
bash tools/migrate.sh BRCA GEXP results_dir
```

Now let's consolidate each model's results into a single file called `preds.tsv` or any name. Again, we specify the cancer cohort and data platform. The last argument are the names of all model methods we have ML predictions from, where each is separated by a `.`. The order of the methods does no matter. (example of the alternative sitation where we only ran SK Grid, AKLIMATE, and CloudForest, then this arugment would be skgrid.aklimate.cloudforest)
```
bash tools/build_results_file.sh preds.tsv results_dir BRCA GEXP skgrid.cloudforest.jadbio.aklimate.subscope
```

**Analysis is now complete!**

The subtype predictions can be found in column `subtype` of the file specified. An example of the format of this file is shown below.

| sampleID  | subtype | TCGA_cohort | platform | group_prediction_details | skgrid_call | skgrid:BRCA_1 | ... | subscope:BRCA_4|
|----|---|---| ---| ---|  ---|  ---|  ---|  ---|
| Sample1 | Subtype1 | cancer | data_platform | Subtype1 |  Subtype1 | 0.93 |  ... | 0.03 |
| Sample2  | Subtype3 | cancer | data_platform | Subtype1:Subtype3 | Subtype3 | 0.21  | ... | 0.44 |
| ...  | ... | ... | ... | ... | ... | ... | ... | ... |
| SampleN | Subtype2 | cancer | data_platform | Subtype1:Subtype2 | Subtype1 | 0.44 | ... | 0.18 |

+ `sampleID` sample ID
+ `subtype` single subtype that was predicted by models with highest confidence  (mean confidence across all ML methods)
+ `TCGA_cohort` cancer cohort abbreviation
+ `platform` data type platform
+ `group_prediction_details` tied subtype calls are allowed if equal number of ML methods picked it (will match `subtype` column if no ties)
+ `skgrid_call` subtype with the highest model confidence by SK Grid (same format for each of the other ML methods)
+ `skgrid:BRCA_1` model confidence that a given sample is this particular subtype (same format for each of the other ML methods)
