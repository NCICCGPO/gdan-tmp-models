#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: docker.synapse.org/syn29568296/jad
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement

inputs:
  model: File[]
  input_data: File[]
  out: string[]


outputs:
  predictionouts:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*_preds.csv"
    outputSource: stepjadbio/predictionouts


steps:
  stepjadbio:
    in:
      model: model
      input_data: input_data
      out: out
    scatter: [model, input_data, out]
    scatterMethod: dotproduct
    out: [predictionouts]
    run: ../tools/jadbio-pred.cwl
