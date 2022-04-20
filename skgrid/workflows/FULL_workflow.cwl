#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: docker.synapse.org/syn29568296/sk_grid
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement


inputs:
  input_data: File[]
  cancer: string[]
  platform: string[]
  output_prefix: string[]

outputs:
  mlib_out:
    type: File[]
    outputBinding:
      glob: "Classifier.*"
    outputSource: create_mlib/mlib_out
  train:
    type: File[]
    outputBinding:
      glob: "*.model"
    outputSource: train_model/train
  pred:
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
      output_prefix: output_prefix
      model: train_model/train
    scatter: [input_data, output_prefix, model]
    scatterMethod: dotproduct
    out: [pred]
    run: ../tools/skgrid-pred.cwl
