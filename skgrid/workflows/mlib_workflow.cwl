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
  cancer: string[]
  platform: string[]

outputs:
  mlib_out:
    type: File[]
    outputBinding:
      glob: "Classifier.*"
    outputSource: create_mlib/mlib_out

steps:
  create_mlib:
    in:
      cancer: cancer
      platform: platform
    scatter: [cancer, platform]
    scatterMethod: dotproduct
    out: [mlib_out]
    run: ../tools/skgrid-mlib.cwl
