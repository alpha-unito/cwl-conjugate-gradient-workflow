cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "split_cols"

inputs:
  script:
    type: File
    inputBinding:
      position: 1
  matrix:
    type: File
    inputBinding:
      position: 3
      prefix: --matrix
  outname:
    type: string
    inputBinding:
      position: 4
      prefix: --outname

outputs:
  vector:
    type: File[]
    outputBinding:
      glob: "$(inputs.outname)*.csv"