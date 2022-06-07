#!/bin/bash
mkdir -p data/model_library
mkdir -p data/src
mkdir -p data/train

# # Run extract model parameters, train model, and predict
# # cwl-runner --outdir data/preds \
cwl-runner --outdir preds \
  workflows/FULL_workflow.cwl \
  ../user-job-ymls/skgrid-inputs.yml

# Clean up
mv preds/Classifier.* data/model_library
mv preds/*.model data/train
echo '###'
echo 'ML model parameters saved in skgrid/data/model_library/'
echo 'Trained ML model pickle saved in skgrid/data/train/'
echo 'Prediction file saved in skgrid/preds/'
echo '###'
