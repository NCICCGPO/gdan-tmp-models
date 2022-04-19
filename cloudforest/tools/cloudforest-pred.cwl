#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [applyforest, -fm, -rfpred, -preds, ./] # name of command to run
requirements:
  InlineJavascriptRequirement: {}
hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/cf


inputs:
  fm_input:
    type: File
    inputBinding:
      position: 1
      prefix: -fm

  rfpred_input:
    type: File
    inputBinding:
      position: 2
      prefix: -rfpred

  preds_input:
    type: string
    inputBinding:
      position: 3
      prefix: -preds

outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "rf_*.cl"
