#!/bin/bash

data=${1}
cancer=${2}
platform=${3}

# Determine which model to use
model=$(python /skgrid/pick_model.py --cancer ${cancer} --platform ${platform})

if [[ ${model} == '' ]]
then
	echo 'Error no model found, check user input {CANCER} and {PLATFORM} values'
else
	# Predict subtypes
	echo 'Selecting best model: ' ${model}
	python /skgrid/prediction_runner.py \
		--data ${data} \
		--cancer  ${cancer} \
		--model "/skgrid/data/train/${model}"
fi
