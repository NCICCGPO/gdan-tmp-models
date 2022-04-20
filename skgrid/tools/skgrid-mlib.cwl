#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/mlib.sh"]
hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/sk_grid

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
    type: File
    outputBinding:
      glob: "Classifier.*"
