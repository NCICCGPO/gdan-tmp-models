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
  platform: string[]

outputs:
  mlib_out:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "Classifier.*"
    outputSource: create_mlib/mlib_out
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
  create_mlib:
    in:
      cancer: cancer
      platform: platform
    scatter: [cancer, platform]
    scatterMethod: dotproduct
    out: [mlib_out]
    run: ../tools/skgrid-mlib.cwl

  train_model:
    in:
      cancer: cancer
      platform: platform
      model_json: create_mlib/mlib_out
    scatter: [cancer, platform, model_json]
    scatterMethod: dotproduct
    out: [train]
    run: ../tools/skgrid-train.cwl

  make_preds:
    in:
      input_data: input_data
      cancer: cancer
      model: train_model/train
    scatter: [input_data, cancer, model]
    scatterMethod: dotproduct
    out: [pred]
    run: ../tools/skgrid-pred.cwl
