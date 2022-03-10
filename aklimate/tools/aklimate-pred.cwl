#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_data)
hints:
  DockerRequirement:
    dockerPull: "aklimate2"


inputs:
  cancer:
    type: string
    inputBinding:
      position: 1

  input_data:
    type: File
    inputBinding:
      position: 2


outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "*_predictions_for_*.tsv"
