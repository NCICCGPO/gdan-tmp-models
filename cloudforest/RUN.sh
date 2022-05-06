#!/bin/bash

input_data=${1}

# Prep input file - transpose
# saves output file into the user-transformed-data dir
python tools/transpose.py ${input_data}

# run cwl tool
cwl-runner --outdir data/preds \
  workflows/ml_workflow.cwl \
  ../user-job-ymls/cloudforest-inputs.yml
