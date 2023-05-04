#!/usr/bin/bash
user_data=${1}
cancer=${2}

# Transform data
python tools/quantile_rescale.py \
	--src ${user_data} \
	--dst skgrid/data/src/training_data/${cancer}_v12_20210228.tsv \
	--out user-transformed-data/transformed-data.tsv
