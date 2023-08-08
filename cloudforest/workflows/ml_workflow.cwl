#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: docker.synapse.org/syn29568296/cloudforest_all
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement

inputs:
  rfpred_input: File[]
  fm_input: File[]
  preds_input: string[]
  votes_input: string[]

outputs:
  predictionouts:
    type: File[]
    outputBinding:
      glob: "*.tsv"
    outputSource: stepcloudforest/predictionouts
  voting_outs:
    type: File[]
    outputBinding:
      glob: "*.vo"
    outputSource: stepcloudforest/voting_outs

steps:
  stepcloudforest:
    in:
      rfpred_input: rfpred_input
      fm_input: fm_input
      preds_input: preds_input
      votes_input: votes_input
    scatter: [rfpred_input, fm_input, preds_input, votes_input]
    scatterMethod: dotproduct
    out: [predictionouts, voting_outs]
    run: ../tools/cloudforest-pred.cwl
