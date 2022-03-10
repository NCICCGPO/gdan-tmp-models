#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "subscope"
    dockerOutputDirectory: "/data"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  cancer: string[]
  platform: string[]
  input_data: File[]


outputs:
  predictionouts:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*.tsv"
    outputSource: stepsubscope/predictionouts


steps:
  stepsubscope:
    in:
      cancer: cancer
      platform: platform
      input_data: input_data
    scatter: [cancer, platform, input_data]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/subscope-pred.cwl
