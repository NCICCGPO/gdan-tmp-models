#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: docker.synapse.org/syn29568296/aklimate
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  cancer: string[]
  platform: string[]
  input_data: File[]


outputs:
  predictionouts:
    type: File[]
    outputBinding:
      glob: "*_predictions_for_*.tsv"
    outputSource: stepaklimate/predictionouts


steps:
  stepaklimate:
    in:
      cancer: cancer
      platform: platform
      input_data: input_data
    scatter: [cancer, platform, input_data]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/aklimate-pred.cwl
