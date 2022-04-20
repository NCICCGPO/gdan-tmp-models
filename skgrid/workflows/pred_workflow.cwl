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
  #cancer: string[]
  output_prefix: string[]
  model: File[]

outputs:
  pred:
    type: File[]
    outputBinding:
      glob: "*_preds.tsv"
    outputSource: make_preds/pred


steps:
  make_preds:
    in:
      input_data: input_data
      #cancer: cancer
      output_prefix: output_prefix
      model: model
    scatter: [input_data, output_prefix, model]
    scatterMethod: dotproduct
    out: [pred]
    run: ../tools/skgrid-pred.cwl
