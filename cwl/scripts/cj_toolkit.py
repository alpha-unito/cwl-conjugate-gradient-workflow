import argparse
from functools import partial
import numpy as np
import os
from pathlib import Path
import time

import functions


def random_vector(args):
    res = functions.initial_solution(args.size)
    print("Generated random vector:", res, sep="\n")
    res.tofile(Path(args.outname).with_suffix(".csv"), sep=",")


def init_vector(args):
    matrix = functions.get_matrix_from_file(args.matrix)
    vector_x = functions.get_matrix_from_file(args.vector_x)[0]
    vector_h = functions.get_matrix_from_file(args.vector_h)[0]
    vector_p, _ = functions.step_1(matrix, vector_x, vector_h)
    print("Generated vector p 0", vector_p)
    vector_p.tofile(Path(args.outname).with_suffix(".csv"), sep=",")


def residual(args):
    vector_a = functions.get_matrix_from_file(args.vector_a)[0]
    vector_b = functions.get_matrix_from_file(args.vector_b)[0]
    value = 1.0
    if args.scalar_value:
        value = functions.get_matrix_from_file(args.scalar_value)[0][0]
    res = vector_a + np.dot(value, vector_b)
    print("Residual vector", res, sep="\n")
    res.tofile(Path(args.outname).with_suffix(".csv"), sep=",")


def split_cols(args):
    format_type = ".csv"
    matrix = functions.get_matrix_from_file(args.matrix)
    base_path = Path(f"{args.outname}").with_suffix(format_type)

    for col in range(np.shape(matrix)[1]):
        path = Path(
            os.path.dirname(base_path),
            f"{os.path.basename(base_path).rsplit('.')[0]}_col_{col}",
        ).with_suffix(format_type)
        matrix[col, :].tofile(path, sep=",")


def dot_product(args):
    vector_a = functions.get_matrix_from_file(args.vector_a)[0]
    vector_b = functions.get_matrix_from_file(args.vector_b)[0]
    # time.sleep(30)
    res = np.dot(vector_a, vector_b)
    print("dot_product", res, sep="\n")
    res.tofile(Path(args.outname).with_suffix(".csv"), sep=",")


def create_vector(args):
    arr = []
    for path in args.inputs:
        with open(path) as fd:
            line = fd.read()
        arr.append(float(line.strip()))
    print("create_vector", arr, sep="\n")
    np.array(arr).tofile(Path(args.outname).with_suffix(".csv"), sep=",")


def vector_division(args):
    vector_a = functions.get_matrix_from_file(args.vector_a)[0]
    vector_b = functions.get_matrix_from_file(args.vector_b)[0]
    if args.vector_c:
        vector_c = functions.get_matrix_from_file(args.vector_c)[0]
    else:
        vector_c = vector_b
    num = np.dot(vector_a, vector_a)
    den = np.dot(vector_b, vector_c)
    res = num / den
    print("vector_division", f"{num} / {den} = {res}", sep="\n")
    with open(Path(args.outname).with_suffix(".csv"), "w") as fd:
        fd.write(str(res))


TOOLS = {
    "init_vector": partial(init_vector),
    "random_vector": partial(random_vector),
    "residual": partial(residual),
    "split_cols": partial(split_cols),
    "dot_product": partial(dot_product),
    "create_vector": partial(create_vector),
    "vector_division": partial(vector_division),
}


def main(args):
    if args.tool not in TOOLS.keys():
        raise Exception(f"Selected an invalid tool {args.tool}")

    TOOLS[args.tool](args)


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(dest="tool")

        # random_vector tool
        random_vector_parser = subparsers.add_parser(
            "random_vector",
            help="Generate random vector",
        )
        random_vector_parser.add_argument(
            "-s",
            "--size",
            help="Insert the vector size",
            type=check_positive,
            required=True,
        )
        random_vector_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # residual tool
        residual_parser = subparsers.add_parser(
            "residual",
            help="vector_a + ( scalar_value * vector_b ) ",
        )
        residual_parser.add_argument(
            "-a",
            "--vector_a",
            help="Insert the vector_a file path",
            type=str,
            required=True,
        )
        residual_parser.add_argument(
            "-b",
            "--vector_b",
            help="Insert the vector_b file path",
            type=str,
            required=True,
        )
        residual_parser.add_argument(
            "-s",
            "--scalar_value",
            help="Insert the scalar file path",
            type=str,
            default=None,
        )
        residual_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # split columns tool
        columns_parser = subparsers.add_parser(
            "split_cols",
            help="Given a matrix, return a file for each column",
        )
        columns_parser.add_argument(
            "-m",
            "--matrix",
            help="Insert the matrix file path",
            type=str,
            required=True,
        )
        columns_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # dot_product tool
        dot_product_parser = subparsers.add_parser(
            "dot_product",
            help="vector_a * vector_b ",
        )
        dot_product_parser.add_argument(
            "-a",
            "--vector_a",
            help="Insert the vector_a file path",
            type=str,
            required=True,
        )
        dot_product_parser.add_argument(
            "-b",
            "--vector_b",
            help="Insert the vector_b file path",
            type=str,
            required=True,
        )
        dot_product_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # create_vector tool
        create_vector_parser = subparsers.add_parser(
            "create_vector",
            help="Create a vector with input elements",
        )
        create_vector_parser.add_argument(
            "-i",
            "--inputs",
            help="Insert the input file path",
            type=str,
            required=True,
            action="append",
        )
        create_vector_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # vector division tool
        vector_division_parser = subparsers.add_parser(
            "vector_division",
            help="< a, a > / < b, c >, where a, b and c are vectors, moreover, if c it is not defined, it is used b\n <a, b> = scalar_product sum_{i=1,N} (a_i * b_i)",
        )
        vector_division_parser.add_argument(
            "-a",
            "--vector_a",
            help="Insert the input file path",
            type=str,
            required=True,
        )
        vector_division_parser.add_argument(
            "-b",
            "--vector_b",
            help="Insert the input file path",
            type=str,
            required=True,
        )
        vector_division_parser.add_argument(
            "-c",
            "--vector_c",
            help="Insert the input file path",
            type=str,
            default=None,
        )
        vector_division_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        # init_vector tool
        init_vector_parser = subparsers.add_parser(
            "init_vector",
            help="Generate init vector: h - Ax",
        )
        init_vector_parser.add_argument(
            "-vh",
            "--vector_h",
            help="Insert the vector_h file path",
            type=str,
            required=True,
        )
        init_vector_parser.add_argument(
            "-m",
            "--matrix",
            help="Insert the matrix file path",
            type=str,
            required=True,
        )
        init_vector_parser.add_argument(
            "-x",
            "--vector_x",
            help="Insert the vector_x file path",
            type=str,
            required=True,
        )
        init_vector_parser.add_argument(
            "-o",
            "--outname",
            help="Insert the output file name",
            type=str,
            required=True,
        )

        args = parser.parse_args()

        if len(args._get_kwargs()) == 1:
            parser.print_help()
        else:
            main(args)
    except KeyboardInterrupt:
        print()
    pass
