#!/bin/bash
#COPY create_grid.py run_learn.py runner.py run_train.py train.sh  ./

# Build full skgrid model library
python scripts/create_grid.py \
	--config data/src/grid.yml  \
	--outdir data/output/model_library -n 1

# Train on TMP data and output trained model (pickle)
python scripts/run_train.py --ft_list data/src/featurelist.txt \
	--ft_file data/src/BRCA_v12_20210228.tsv \
	--model data/output/model_library/RandomForestClassifier.11 \
	--out data/output/train
