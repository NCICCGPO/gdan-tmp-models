#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: Workflow
requirements:
  - class: DockerRequirement
    dockerPull: "skgrid"
  - class: ScatterFeatureRequirement
  - class: StepInputExpressionRequirement
  - class: SubworkflowFeatureRequirement

inputs: []

outputs:
  mlib_out:
    doc: tbd
    type:
      type: array
      items: File
    outputBinding:
      glob: "Classifier.*"
    outputSource: create_mlib/mlib_out


steps:
  create_mlib:
    in: []
    out: [mlib_out]
    run: ../tools/skgrid-mlib.cwl
