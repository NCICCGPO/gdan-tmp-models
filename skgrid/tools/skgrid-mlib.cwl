#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["/skgrid/mlib.sh"]
hints:
  DockerRequirement:
    dockerPull: "skgrid"


inputs:
  model_config:
    type: File
    inputBinding:
      position: 1


outputs:
  mlib_out:
    type: File
    outputBinding:
      glob: "*RandomForestClassifier.11"
