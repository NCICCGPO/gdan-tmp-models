#!/bin/bash

echo 'Building model library and training ML models'
# Build full skgrid model library
python /skgrid/create_grid.py \
	--config /skgrid/data/src/grid.yml

	# --config ${model_config}
	# --config data/src/grid.yml  \
	# --outdir data/model_library -n 1
#
