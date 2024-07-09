cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "init_vector"

inputs:
  script:
    type: File
    inputBinding:
      position: 1
  vector_h:
    type: File
    inputBinding:
      position: 3
      prefix: --vector_h
  matrix:
    type: File
    inputBinding:
      position: 4
      prefix: --matrix
  vector_x:
    type: File
    inputBinding:
      position: 5
      prefix: --vector_x
  outname:
    type: string
    inputBinding:
      position: 6
      prefix: --outname

outputs:
  vector:
    type: File
    outputBinding:
      glob: "$(inputs.outname).csv"