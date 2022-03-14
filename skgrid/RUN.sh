#!/usr/bin/bash

# Build full skgrid model library
python create_grid.py data/src/grid.yml  --outdir data/output/model_library -n 1

# Train on TMP data and output trained model (pickle)
python run_train.py --feature_list data/src/featurelist.txt --feat_file data/src/BRCA_v12_20210228.tsv --hypr_file data/output/model_library/RandomForestClassifier.11 --output data/output/train

# Predict subtypes
python runner.py data/src/BRCA_v12_20210228.tsv data/output/preds/BRCA_preds.tsv data/output/train/RandomForestClassifier-criterion-entropy_n_estimators-200.model
