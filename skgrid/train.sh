#!/bin/bash
cancer=${1}
platform=${2}
# echo 'Building model library and training ML models'

# # Build full skgrid model library
# python image_scripts/create_grid.py \
# 	--config data/src/grid.yml  \
# 	--outdir data/model_library -n 1

# Train on TMP data and output trained model in train/ (pickle)
echo 'Training model'
python /skgrid/run_train.py \
	--ft_list /skgrid/data/src/training_data/${cancer}_${platform}_featurelist.txt \
	--ft_file /skgrid/data/src/training_data/${cancer}_v12_20210228.tsv \
	--platform ${platform} \
	--cancer ${cancer}
