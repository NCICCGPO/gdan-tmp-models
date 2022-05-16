#!/bin/bash

input_data=${1}

# run cwl tool
cwl-runner --outdir preds \
  workflows/ml_workflow.cwl \
  ../user-job-ymls/cloudforest-inputs.yml
