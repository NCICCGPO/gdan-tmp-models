#!/bin/bash
cancer=${1}
platform=${2}
model_json=${3}
# Train on TMP data and output trained model in train/ (pickle)
echo 'Training model'
python /skgrid/run_train.py \
	--ft_list /skgrid/data/src/training_data/${cancer}_${platform}_featurelist.txt \
	--ft_file /skgrid/data/src/training_data/${cancer}_v12_20210228.tsv \
	--platform ${platform} \
	--cancer ${cancer} \
	--model_file ${model_json}
