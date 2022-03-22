#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/mlib.sh"]
hints:
  DockerRequirement:
    dockerPull: "skgrid"

inputs: []

outputs:
  mlib_out:
    type:
      type: array
      items: File
    outputBinding:
      glob: "Classifier.*"
