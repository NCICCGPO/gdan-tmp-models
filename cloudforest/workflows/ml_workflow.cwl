#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: docker.synapse.org/syn29568296/cf
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement





inputs:
  fm_input: File[]
    #doc: tbd
    #type: File
  rfpred_input: File[]
    #doc: tbd
    #type: File
  preds_input: string[]
    #doc: tbd
    #type: string





outputs:
  predictionouts:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "rf_*.cl"
    outputSource: stepcloudforest/predictionouts





steps:
  stepcloudforest:
    in:
      fm_input: fm_input
      rfpred_input: rfpred_input
      preds_input: preds_input
    scatter: [fm_input, rfpred_input, preds_input]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/cloudforest-pred.cwl
