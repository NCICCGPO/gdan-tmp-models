#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/mlib.sh"]
hints:
  DockerRequirement:
    dockerImageId: "skgrid"

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
  mlib_out:
    doc: tbd
    type: File
    outputBinding:
      glob: "Classifier.*"
