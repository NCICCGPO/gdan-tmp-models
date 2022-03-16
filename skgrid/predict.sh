#!/bin/bash
# Predict subtypes
data=${1}
cancer=${2}
model=${3}
python /skgrid/prediction_runner.py \
	--data ${data} \
	--cancer  ${cancer} \
	--model ${model}
