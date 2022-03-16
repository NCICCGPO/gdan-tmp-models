#!/bin/bash

data=${1}
cancer=${2}
# model=${3}
platform=GEXP

# Determine which model to use
model=$(python /skgrid/pick_model.py --cancer ${cancer} --platform ${platform})

# Predict subtypes
python /skgrid/prediction_runner.py \
	--data ${data} \
	--cancer  ${cancer} \
	--model "/skgrid/data/train/${model}"
