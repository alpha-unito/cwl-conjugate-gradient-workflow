cwlVersion: v1.2
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}

baseCommand: [ "python"]
arguments:
  - position: 2
    valueFrom: "create_vector"

inputs:
  script:
    type: File
    inputBinding:
      position: 1
  scalars:
    type:
      type: array
      items: File
      inputBinding:
        prefix: "--inputs"
    inputBinding:
      position: 3
  outname:
    type: string
    inputBinding:
      position: 4
      prefix: --outname

outputs:
  vector:
    type: File
    outputBinding:
      glob: "$(inputs.outname)*.csv"