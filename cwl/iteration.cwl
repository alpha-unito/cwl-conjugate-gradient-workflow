#!/usr/bin/env cwl-runner
cwlVersion: v1.2
class: Workflow
$namespaces:
  sf: "https://streamflow.org/cwl#"

requirements:
  ScatterFeatureRequirement: { }

inputs:
  script: File
  vector_x: File
  vector_p: File
  vector_r: File
  matrix: File
  index: int
  max_iterations: int
  column_str: string


outputs:
  - id: vector_x_next
    type: File
    outputSource: generate_x/vector
  - id: vector_p_next
    type: File
    outputSource: generate_p/vector
  - id: vector_r_next
    type: File
    outputSource: generate_r/vector

steps:
  split_matrix:
    run: clt/split_matrix.cwl
    in:
      script: script
      matrix: matrix
      outname:
        default: "column"
    out:
      [ vector ]

  column_p:
    run: clt/dot_product.cwl
    in:
      script: script
      vector_a: split_matrix/vector
      vector_b: vector_p
      outname: column_str
    scatter: vector_a
    out:
      [ scalar ]

  reduction:
    run: clt/reduction.cwl
    in:
      script: script
      scalars: column_p/scalar
      outname:
        default: "vector_q"
    out:
      [ vector ]

  ##############################################################



  generate_alpha:
    run: clt/division_vectors.cwl
    in:
      script: script
      vector_a: vector_r
      vector_b: vector_p
      vector_c: reduction/vector
      outname:
        default: "alpha"
    out:
      [ scalar ]


  generate_x:
    run: clt/residual.cwl
    doc: vector_a + scalar * vector_b
    in:
      script: script
      vector_a: vector_x
      scalar: generate_alpha/scalar
      vector_b: vector_p
      negative:
        default: false
      outname:
        default: "vector_x"
    out:
      [ vector ]

  generate_r:
    run: clt/residual.cwl
    doc: vector_a - scalar * vector_b
    in:
      script: script
      vector_a: vector_r
      scalar: generate_alpha/scalar
      negative:
        default: true
      vector_b: vector_p
      outname:
        default: "vector_r"
    out:
      [ vector ]


  generate_beta:
    run: clt/division_vectors.cwl
    in:
      script: script
      vector_a: generate_r/vector
      vector_b: vector_r
      outname:
        default: "beta"
    out:
      [ scalar ]


  generate_p:
    run: clt/residual.cwl
    doc: vector_a + scalar * vector_b
    in:
      script: script
      vector_a: generate_r/vector
      scalar: generate_beta/scalar
      vector_b: vector_p
      negative:
        default: false
      outname:
        default: "vector_p"
    out:
      [ vector ]