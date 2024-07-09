cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "random_vector"

inputs:
  script:
    type: File
    inputBinding:
      position: 1
  length:
    type: int
    inputBinding:
      position: 3
      prefix: --size
  outname:
    type: string
    inputBinding:
      position: 4
      prefix: --outname

outputs:
  vector:
    type: File
    outputBinding:
      glob: "$(inputs.outname).csv"