#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_data)
hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/aklimate


inputs:
  cancer:
    type: string
    inputBinding:
      position: 1
  platform:
    type: string
    inputBinding:
      position: 2
  input_data:
    type: File
    inputBinding:
      position: 3


outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "*_predictions_for_*.tsv"
