#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "subscope"
    dockerOutputDirectory: "/data/results"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  cancer: string[]
  platform: string[]
  input_data: File[]


outputs:
  combined_results:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*results.txt"
    outputSource: stepsubscope/combined_results
  combined_confidence:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*confidence.txt"
    outputSource: stepsubscope/combined_confidence
  model1:
    type: Directory[]
    outputBinding:
      glob: "*model1"
    outputSource: stepsubscope/model1
  model2:
    type: Directory[]
    outputBinding:
      glob: "*model2"
    outputSource: stepsubscope/model2
  model3:
    type: Directory[]
    outputBinding:
      glob: "*model3"
    outputSource: stepsubscope/model3
  model4:
    type: Directory[]
    outputBinding:
      glob: "*model4"
    outputSource: stepsubscope/model4
  model5:
    type: Directory[]
    outputBinding:
      glob: "*model5"
    outputSource: stepsubscope/model5

steps:
  stepsubscope:
    in:
      cancer: cancer
      platform: platform
      input_data: input_data
    scatter: [cancer, platform, input_data]
    scatterMethod: dotproduct
    out: [combined_results, combined_confidence, model1, model2, model3, model4, model5]
    run: ../tools/subscope-pred.cwl
