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
  rfpred_input: File[]
  fm_input: File[]
  preds_input: string[]





outputs:
  predictionouts:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*.tsv"
    outputSource: stepcloudforest/predictionouts





steps:
  stepcloudforest:
    in:
      rfpred_input: rfpred_input
      fm_input: fm_input
      preds_input: preds_input
    scatter: [rfpred_input, fm_input, preds_input]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/cloudforest-pred.cwl
