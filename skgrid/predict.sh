#!/bin/bash

data=${1}
out=${2}
model=${3}

# Example:
# data=data/src/BRCA_v12_20210228.tsv
# out=data/output/preds/BRCA_preds.tsv
# model=data/output/train/RandomForestClassifier-criterion-entropy_n_estimators-200.model

# Predict subtypes
python runner.py \
	--data ${data} \
	--out  ${out} \
	--trained ${model}
