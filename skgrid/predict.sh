#!/bin/bash

data=${1}
cancer=${2}
model=${3}

# Example:
# data=data/src/BRCA_v12_20210228.tsv
# cancer=BRCA
# model=data/output/train/RandomForestClassifier-criterion-entropy_n_estimators-200.model



# Predict subtypes
python /skgrid/prediction_runner.py \
	--data ${data} \
	--cancer  ${cancer} \
	--trained ${model}
