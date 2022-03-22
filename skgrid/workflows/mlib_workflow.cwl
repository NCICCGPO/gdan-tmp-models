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
  model_config: File[]

outputs:
  mlib_out:
    doc: tbd
    type: File[]
    outputBinding:
      glob: "*RandomForestClassifier.11"
    outputSource: create_mlib/mlib_out



steps:
  create_mlib:
    in:
      model_config: model_config
    scatter: [model_config]
    scatterMethod: dotproduct
    out: [mlib_out]
    run: ../tools/skgrid-mlib.cwl
