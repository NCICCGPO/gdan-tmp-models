#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [java, --enable-preview, -jar, /src/jadbio-model-exe.jar]
requirements:
  InlineJavascriptRequirement: {}
hints:
  DockerRequirement:
    dockerPull: "jadbio"


inputs:
  model:
    type: File
    inputBinding:
      position: 4
      prefix: --model

  input_data:
    type: File
    inputBinding:
      position: 5
      prefix: --input

  out:
    type: string
    inputBinding:
      position: 6
      prefix: --output

outputs:
  predictionouts:
    type: File
    outputBinding:
      glob: "*_preds.csv"
