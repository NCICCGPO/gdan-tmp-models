#!/bin/bash

# run cwl tool
cwl-runner --outdir data/preds \
  workflows/ml_workflow.cwl \
  job_inputs/skgrid-inputs.yml
