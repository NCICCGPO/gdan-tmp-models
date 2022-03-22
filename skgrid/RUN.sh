#!/bin/bash

mkdir -p data/input
mkdir -p data/model_library
mkdir -p data/preds
mkdir -p data/src
mkdir -p data/train

# # run model training
# # cwl-runner --outdir data/train \
# cwl-runner \
#   workflows/train_workflow.cwl \
#   job_inputs/skgrid-train-inputs.yml
# mv *.model data/train

# COMPLETE - run predictions
# cwl-runner --outdir data/preds \
cwl-runner \
  workflows/ml_workflow.cwl \
  job_inputs/skgrid-inputs.yml
mv *_preds.tsv data/preds
