#!/bin/bash

mkdir -p data/input
mkdir -p data/model_library
mkdir -p data/preds
mkdir -p data/src
mkdir -p data/train

# run cwl tool
cwl-runner --outdir data/preds \
  workflows/ml_workflow.cwl \
  job_inputs/skgrid-inputs.yml
