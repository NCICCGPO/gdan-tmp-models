#!/bin/bash
cancer=${1}
platform=${2}
echo 'Building model library and training ML models'
# Build full skgrid model library
python /skgrid/set_model_params.py \
	--config /skgrid/data/src/grid.yml \
	--cancer ${cancer} \
	--platform ${platform}
