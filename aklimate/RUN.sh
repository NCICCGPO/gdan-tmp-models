#!/bin/bash

# run cwl tool
cwl-runner --outdir data/preds \
  workflows/ml_workflow.cwl \
  ../user-job-ymls/aklimate.yml
