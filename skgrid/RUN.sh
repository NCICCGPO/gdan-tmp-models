#!/bin/bash
mkdir -p data/input
mkdir -p data/model_library
mkdir -p data/preds
mkdir -p data/src
mkdir -p data/train

# # Run extract model parameters, train model, and predict
# # cwl-runner --outdir data/preds \
cwl-runner \
  workflows/FULL_workflow.cwl \
  job_inputs/skgrid-FULL-inputs.yml

# Clean up
mv Classifier.* data/model_library
mv *.model data/train
mv *_preds.tsv data/preds
echo '###'
echo 'ML model parameters saved in data/model_library/'
echo 'Trained ML model pickle saved in data/train/'
echo 'Prediction file saved in data/preds/'
echo '###'
