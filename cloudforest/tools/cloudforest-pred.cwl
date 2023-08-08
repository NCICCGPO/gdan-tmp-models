#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [applyforest, -rfpred, -fm, -preds, -votes ] # name of command to run
requirements:
  InlineJavascriptRequirement: {}


hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/cloudforest_all


inputs:
  rfpred_input:
    type: File
    inputBinding:
      position: 1
      prefix: -rfpred

  fm_input:
    type: File
    inputBinding:
      position: 2
      prefix: -fm

  preds_input:
    type: string
    inputBinding:
      position: 3
      prefix: -preds

  votes_input:
    type: string
    inputBinding:
      position: 4
      prefix: -votes

outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "*.tsv"
  voting_outs:
    type: File
    outputBinding:
      glob: "*.vo"
