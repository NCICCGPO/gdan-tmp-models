#!/usr/bin/bash

# Purpose: move the ML results into a predictions directory
cancer=${1} # ex. BRCA
platform=${2} # ex. GEXP
results_dir=${3} # ex. results_dir

# Set up results dir to hold subtype predictions
mkdir -p ${results_dir}/${cancer}
mkdir -p ${results_dir}/midway

# Move files, there will be an error message if any of these 5 methods didn't work
mv skgrid/preds/${cancer}_${platform}_skgrid_preds.tsv ${results_dir}/${cancer}/
mv jadbio/preds/${cancer}* ${results_dir}/${cancer}/
mv cloudforest/preds/${cancer}* ${results_dir}/${cancer}/

mv aklimate/preds/${cancer}* aklimate/preds/${1}_${2}_aklimate_preds.tsv
mv aklimate/preds/${cancer}* ${results_dir}/${cancer}/

mkdir ${results_dir}/${cancer}/subscope_additional_files
mv subscope/preds/* ${results_dir}/${cancer}/
mv ${results_dir}/${cancer}/${platform}-model* ${results_dir}/${cancer}/subscope_additional_files/
mv ${results_dir}/${cancer}/${platform}-subscope-results.txt ${results_dir}/${cancer}/${1}_${2}_subscope_preds.tsv
mv ${results_dir}/${cancer}/${platform}-subscope-confidence.txt ${results_dir}/${cancer}/${1}_${2}_subscope_confidence.tsv
