#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "cloudforest"





inputs:
  fm:
    doc: tbd
    type: File
  rfpred:
    doc: tbd
    type: File
  preds:
    doc: tbd
    type: string





outputs:
  predictionouts:
    doc: tbd
    type: File
    outputBinding:
      glob: "*.cl"
    outputSource: stepcloudforest/predictionouts





steps:
  # Cloudforest
  stepcloudforest:
    run: ../tools/cloudforest-pred.cwl
    in:
      fm: fm
      rfpred: rfpred
      preds: preds
    out: [predictionouts]
