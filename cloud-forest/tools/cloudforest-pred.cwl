#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [applyforest, -fm, -rfpred, -preds, ./] # name of command to run
requirements:
  InlineJavascriptRequirement: {}
hints:
  DockerRequirement:
    dockerPull: "cloudforest"


inputs:
  # fm input file
  fm:
    type: File
    inputBinding:
      position: 1
      prefix: -fm

  # rfpred file
  rfpred:
    type: File
    inputBinding:
      position: 2
      prefix: -rfpred

  preds:
    type: string
    inputBinding:
      position: 3
      prefix: -preds

outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "rf_1_4_1_1_3.cl"
