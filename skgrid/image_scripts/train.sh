#!/bin/bash
# Build full skgrid model library
python image_scripts/create_grid.py \
	--config data/src/grid.yml  \
	--outdir data/model_library -n 1

# Train on TMP data and output trained model (pickle)
python image_scripts/run_train.py --ft_list data/src/featurelist.txt \
	--ft_file data/src/BRCA_v12_20210228.tsv \
	--model data/model_library/RandomForestClassifier.11 \
	--out data/train
