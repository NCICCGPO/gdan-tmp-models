#!/bin/bash
cancer=${1}
platform=${2}
echo 'Building model library and training ML models'

# Build full skgrid model library
python image_scripts/create_grid.py \
	--config data/src/grid.yml  \
	--outdir data/model_library -n 1

# Train on TMP data and output trained model (pickle)
python image_scripts/run_train.py \
	--ft_list data/src/training_data/${cancer}_${platform}_featurelist.txt \
	--ft_file data/src/training_data/${cancer}_v12_20210228.tsv \
	--platform ${platform} \
	--cancer ${cancer} \
	--out data/train
