#!/bin/bash
mkdir -p data/model_library
mkdir -p data/src
mkdir -p data/train

# # Run extract model parameters, train model, and predict
cwl-runner --outdir preds \
  workflows/FULL_workflow.cwl \
  ../user-job-ymls/skgrid-inputs.yml

# Clean up
mv preds/Classifier.* data/model_library
mv preds/*.model data/train
