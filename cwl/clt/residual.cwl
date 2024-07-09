cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "residual"

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
  scalar:
    type: File
    inputBinding:
      position: 5
      prefix: --scalar_value
  negative:
    type: boolean
  outname:
    type: string
    inputBinding:
      position: 6
      prefix: --outname

outputs:
  vector:
    type: File
    outputBinding:
      glob: "$(inputs.outname)*.csv"