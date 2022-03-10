#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "aklimate2"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  cancer: string[]
  input_data: File[]


outputs:
  predictionouts:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*_predictions_for_*.tsv"
    outputSource: stepaklimate/predictionouts


steps:
  stepaklimate:
    in:
      cancer: cancer
      input_data: input_data
    scatter: [cancer, input_data]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/aklimate-pred.cwl
