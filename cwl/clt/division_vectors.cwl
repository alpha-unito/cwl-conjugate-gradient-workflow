cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "vector_division"

inputs:
  script:
    type: File
    inputBinding:
      position: 1
  vector_a:
    type: File
    inputBinding:
      position: 3
      prefix: --vector_a
  vector_b:
    type: File
    inputBinding:
      position: 4
      prefix: --vector_b
  vector_c:
    type: File?
    inputBinding:
      position: 5
      prefix: --vector_c
  outname:
    type: string
    inputBinding:
      position: 6
      prefix: --outname

outputs:
  scalar:
    type: File
    outputBinding:
      glob: "$(inputs.outname)*.csv"