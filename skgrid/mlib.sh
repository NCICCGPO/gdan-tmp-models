#!/bin/bash
model_config=${1}

echo 'Building model library and training ML models'
# Build full skgrid model library
python /skgrid/create_grid.py \
	--config ${model_config}

	
	# --config data/src/grid.yml  \
	# --outdir data/model_library -n 1
#
