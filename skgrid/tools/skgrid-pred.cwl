#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/predict.sh"]
requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_data)
hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/sk_grid


inputs:
  input_data:
    type: File
    inputBinding:
      position: 1
  output_prefix:
    type: string
    inputBinding:
      position: 2
  model:
    type: File
    inputBinding:
      position: 3


outputs:
  pred:
    type: File
    outputBinding:
      glob: "*_preds.tsv"
