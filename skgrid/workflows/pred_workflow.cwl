#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerImageId: "skgrid"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  input_data: File[]
  cancer: string[]

outputs:
  pred:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*_preds.tsv"
    outputSource: make_preds/pred


steps:
  make_preds:
    in:
      input_data: input_data
      cancer: cancer
    scatter: [input_data, cancer]
    scatterMethod: dotproduct
    out: [pred]
    run: ../tools/skgrid-pred.cwl
