#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "skgrid"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  input_data: File[]
  cancer: string[]
  platform: string[]

outputs:
  train:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*.model"
    outputSource: train_model/train
  pred:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*_preds.tsv"
    outputSource: make_preds/pred


steps:
  train_model:
    in:
      cancer: cancer
      platform: platform
    scatter: [cancer, platform]
    scatterMethod: dotproduct
    out: [train]
    run: ../tools/skgrid-train.cwl
  make_preds:
    in:
      input_data: input_data
      cancer: cancer
      platform: platform
    scatter: [input_data, cancer, platform]
    scatterMethod: dotproduct
    out: [pred]
    run: ../tools/skgrid-pred.cwl
