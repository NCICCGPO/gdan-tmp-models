#!/bin/bash

mkdir -p data/input
mkdir -p data/model_library
mkdir -p data/preds
mkdir -p data/src
mkdir -p data/train

# Create model library
cwl-runner \
  workflows/mlib_workflow.cwl
mv Classifier.* data/model_library


# # Run model training, predictions
# # cwl-runner --outdir data/preds \
# cwl-runner \
#   workflows/FULL_workflow.cwl \
#   job_inputs/skgrid-FULL-inputs.yml
# mv *.model data/train
# mv *_preds.tsv data/preds
