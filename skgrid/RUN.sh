#!/usr/bin/bash

# Build full skgrid model library
python create_grid.py \
	--config data/src/grid.yml  \
	--outdir data/output/model_library -n 1

# Train on TMP data and output trained model (pickle)
python run_train.py --ft_list data/src/featurelist.txt \
	--ft_file data/src/BRCA_v12_20210228.tsv \
	--model data/output/model_library/RandomForestClassifier.11 \
	--out data/output/train

# Predict subtypes
python runner.py \
	--data data/src/BRCA_v12_20210228.tsv \
	--out data/output/preds/BRCA_preds.tsv \
	--trained data/output/train/RandomForestClassifier-criterion-entropy_n_estimators-200.model
