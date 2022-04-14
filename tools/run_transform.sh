#!/usr/bin/bash
user_data=${1}

# Transform data
python tools/quantile_rescale.py \
	--src ${user_data} \
	--dst skgrid/data/src/training_data/BRCA_v12_20210228.tsv \
	--out user-transformed-data/transformed-data.tsv
