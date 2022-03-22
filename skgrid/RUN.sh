#!/bin/bash

mkdir -p data/input
mkdir -p data/model_library
mkdir -p data/preds
mkdir -p data/src
mkdir -p data/train

# Run model training, predictions
# cwl-runner --outdir data/preds \
cwl-runner \
  workflows/FULL_workflow.cwl \
  job_inputs/skgrid-FULL-inputs.yml
mv *.model data/train
mv *_preds.tsv data/preds
