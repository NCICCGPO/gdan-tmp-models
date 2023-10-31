#!/usr/bin/bash

set -e

final_file_name=${1} # <name of final results file>
prediction_dir=${2} # results_dir
cancer=${3} # BRCA
platform=${4} # GEXP
methods=${5} # skgrid.cloudforest.jadbio.aklimate.subscope
# List as many cancer cohorts you'd like to get results for
python tools/collate_labels.py \
	--input_dir ${prediction_dir} \
	-o ${prediction_dir}/midway/midway.subtype_predictions_${cancer}_${platform}.tsv \
	-c ${cancer} \
	-p ${platform} \
	--method_list ${methods}
# Add model probabilities
python tools/collate_probs.py \
	--input_dir ${prediction_dir} \
	-c ${cancer} \
	--infile ${prediction_dir}/midway/midway.subtype_predictions_${cancer}_${platform}.tsv \
	--output_dir ${prediction_dir} \
	-p ${platform} \
	--method_list ${methods}
# Finally, merge all results
# if getting results from only one cancer, then add "--single_cancer <CANCER>"
python tools/format_results.py \
	--input_dir ${prediction_dir} \
	--outfile ${prediction_dir}/${final_file_name} \
	--method_list ${methods} \
	-c ${cancer}

rm ${prediction_dir}/midway/*
