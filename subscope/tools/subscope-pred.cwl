#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_data)
hints:
  DockerRequirement:
    dockerPull: docker.synapse.org/syn29568296/subs
    dockerOutputDirectory: "/data/results"


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
  combined_results:
    type: File
    outputBinding:
      glob: "*results.txt"
  combined_confidence:
    type: File
    outputBinding:
      glob: "*confidence.txt"
  model1:
    type: Directory
    outputBinding:
      glob: "*model1"
  model2:
    type: Directory
    outputBinding:
      glob: "*model2"
  model3:
    type: Directory
    outputBinding:
      glob: "*model3"
  model4:
    type: Directory
    outputBinding:
      glob: "*model4"
  model5:
    type: Directory
    outputBinding:
      glob: "*model5"
