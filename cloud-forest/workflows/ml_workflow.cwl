#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "cloudforest"





inputs:
  fm_input:
    doc: tbd
    type: File
  rfpred_input:
    doc: tbd
    type: File
  preds_input:
    doc: tbd
    type: string





outputs:
  predictionouts:
    doc: tbd
    type: File
    outputBinding:
      glob: "rf_*.cl"
    outputSource: stepcloudforest/predictionouts





steps:
  # Cloudforest
  stepcloudforest:
    run: ../tools/cloudforest-pred.cwl
    in:
      fm_input: fm_input
      rfpred_input: rfpred_input
      preds_input: preds_input
    out: [predictionouts]
