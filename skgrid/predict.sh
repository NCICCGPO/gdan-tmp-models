#!/bin/bash

data=${1}
cancer=${2}
# platform=${3}
model=${3}

	# Predict subtypes
	echo 'Selecting best model: ' ${model}
	python /skgrid/prediction_runner.py \
		--data ${data} \
		--cancer  ${cancer} \
		--model ${model}
