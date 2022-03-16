#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_data)
hints:
  DockerRequirement:
    dockerPull: "skgrid"


inputs:
  input_data:
    type: File
    inputBinding:
      position: 1
  cancer:
    type: string
    inputBinding:
      position: 2
  platform:
    type: string
    inputBinding:
      position: 3



outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "*_preds.tsv"
