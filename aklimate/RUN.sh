#!/bin/bash

# run cwl tool
cwl-runner --outdir preds \
  workflows/ml_workflow.cwl \
  ../user-job-ymls/aklimate-inputs.yml
