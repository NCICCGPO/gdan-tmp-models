#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/train.sh"]
hints:
  DockerRequirement:
    dockerImageId: docker.synapse.org/syn29568296/sk_grid


inputs:
  cancer:
    type: string
    inputBinding:
      position: 1
  platform:
    type: string
    inputBinding:
      position: 2
  model_json:
    type: File
    inputBinding:
      position: 3

outputs:
  train:
    type: File
    outputBinding:
      glob: "*.model"
