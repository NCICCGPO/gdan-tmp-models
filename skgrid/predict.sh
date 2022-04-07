#!/bin/bash

data=${1}
output_prefix=${2}
model=${3}


	# Predict subtypes
	echo 'Selecting best model: ' ${model}
	python /skgrid/prediction_runner.py \
		--data ${data} \
		--output_prefix ${output_prefix} \
		--model ${model}
