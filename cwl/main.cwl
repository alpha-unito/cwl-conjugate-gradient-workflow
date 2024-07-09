#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow

requirements:
  InlineJavascriptRequirement: {}
  StepInputExpressionRequirement: {}
  SubworkflowFeatureRequirement: {}

$namespaces:
  cwltool: "http://commonwl.org/cwltool#"
  s: https://schema.org/

$schemas:
 - https://schema.org/version/latest/schemaorg-current-http.rdf

inputs:
  script: File
  vector_h: File
  matrix: File
  length: int
  column_str: string


outputs:
  result:
    type: File
    outputSource: iterations/vector_x_next

steps:

  random_x:
    run: clt/random_vector.cwl
    in:
      script: script
      length: length
      outname:
        default: "vector_x_0"
    out:
      [ vector ]

  init_vector:
    run: clt/init_vector.cwl
    in:
      script: script
      vector_h: vector_h
      matrix: matrix
      vector_x: random_x/vector
      outname:
        default: "residual_0"
    out:
      [ vector ]


  iterations:
    in:
      script: script
      vector_x: random_x/vector
      vector_p: init_vector/vector
      vector_r: init_vector/vector
      matrix: matrix
      index:
        default: 0
      max_iterations: length
      column_str: column_str
    out:
      - id: vector_x_next
      - id: vector_p_next
      - id: vector_r_next
    requirements:
      cwltool:Loop:
        loopWhen: $(inputs.index < inputs.max_iterations)
        loop:
          index:
            valueFrom: $(inputs.index + 1)
          vector_x: vector_x_next
          vector_p: vector_p_next
          vector_r: vector_r_next
        outputMethod: last
    run: iteration.cwl
