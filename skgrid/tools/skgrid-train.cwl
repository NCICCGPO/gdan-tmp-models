#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/train.sh"]
hints:
  DockerRequirement:
    dockerPull: "skgrid"


inputs:
  cancer:
    type: string
    inputBinding:
      position: 1
  platform:
    type: string
    inputBinding:
      position: 2


outputs:
  train:
    type: File
    outputBinding:
      glob: "*.model"