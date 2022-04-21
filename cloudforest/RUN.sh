#!/bin/bash

# run cwl tool
cwl-runner --outdir CF_For_Docker/KIRCKICH/CL \
  workflows/ml_workflow.cwl \
  ../user-job-ymls/cloudforest.yml
