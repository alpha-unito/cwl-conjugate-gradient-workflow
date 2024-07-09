import argparse
import functions
import numpy as np


def main(args):
    init_matrix = functions.get_matrix_from_file(args.matrix)
    print("init matrix:\n", init_matrix)
    functions.check_constraints(init_matrix)
    cap_k = np.shape(init_matrix)[0]

    vector_h = functions.get_matrix_from_file(args.vector_h)[0]
    print("vector_h:", vector_h)
    print()

    if args.x_zero:
        x_0 = functions.get_matrix_from_file(args.x_zero)[0]
    else:
        x_0 = functions.initial_solution(cap_k)
    print("init solution x_0:", x_0)
    print()

    p_0, r_0 = functions.step_1(init_matrix, x_0, vector_h)

    x_array = [x_0]
    p_array = [p_0]
    r_array = [r_0]
    for k in range(0, cap_k):
        print(f"Iteration {k}")
        a_k_next = functions.step_2(r_array[-1], p_array[-1], init_matrix)

        x_k_next = functions.step_3(x_array[-1], a_k_next, p_array[-1])
        x_array.append(x_k_next)

        r_k_next = functions.step_4(r_array[-1], a_k_next, init_matrix, p_array[-1])
        r_array.append(r_k_next)

        b_k_next = functions.step_5(r_array[-1], r_array[-2])

        p_k_next = functions.step_6(r_array[-1], b_k_next, p_array[-1])
        p_array.append(p_k_next)
        print()
    print(f"Solution x_{k}: {x_array[-1]}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-m",
            "--matrix",
            help="Insert path of file with the matrix",
            type=str,
            required=True,
        )
        parser.add_argument(
            "-v",
            "--vector_h",
            help="Insert path of file with the h vector",
            type=str,
            required=True,
        )
        parser.add_argument(
            "-z", "--x_zero", help="Insert path of file with the x_0 vector", type=str
        )
        args = parser.parse_args()
        main(args)
    except KeyboardInterrupt:
        print()
    pass
