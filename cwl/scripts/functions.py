import numpy as np


def get_matrix_from_file(filepath):
    with open(filepath) as fd:
        return np.array(
            [[float(num) for num in line.strip().split(",")] for line in fd.readlines()]
        )


def check_constraints(matrix):
    n_rows, n_columns = np.shape(matrix)
    if n_rows == n_columns:
        print(f"Contraint satisfied: It is a square matrix {n_rows} x {n_columns}")
    else:
        raise Exception(
            f"Contraint NOT satisfied: Matrix must be a square matrix. Instead it is {n_rows} x {n_columns}"
        )

    transpose = np.transpose(matrix)
    if np.array_equal(matrix, transpose):
        print("Contraint satisfied: Matrix is symmetric")
    else:
        raise Exception(f"Contraint NOT satisfied: Matrix is not symmetric")


def initial_solution(size):
    # return np.random.randint(5, size=size)
    return np.random.rand(size)
    # return np.array([ i for i in range(size) ])


def matrix_vector_product(matrix, vector):
    # new_matrix = []
    # todo: eseguire in parallelo questo for . Le iterazioni sono indipendenti
    # for col in range(np.shape(matrix)[0]):
    #     new_matrix.append(np.dot(matrix[col,:], vector))
    # return np.array(new_matrix)
    return np.matmul(matrix, vector)


def step_1(init_matrix, x_0, vector_h):
    cap_a__x_0 = matrix_vector_product(init_matrix, x_0)
    p_0 = r_0 = vector_h - cap_a__x_0
    print(f"step_1: p_0 = r_0 = {p_0}")
    return p_0, r_0


def step_2(r_k, p_k, matrix):
    num = np.dot(r_k, np.transpose(r_k))
    mat = matrix_vector_product(matrix, p_k)
    den = np.dot(p_k, mat)
    res = num / den
    print(f"step_2: {num} / {den} = {res}")
    return res


def step_3(x_k, a_k_next, p_k):
    res = x_k + np.dot(a_k_next, p_k)
    print(f"step_3: {res}")
    return res


def step_4(r_k, a_k_next, cap_a, p_k):
    snd = np.dot(a_k_next, matrix_vector_product(cap_a, p_k))
    res = r_k - snd
    print(f"step_4: {res}")
    return res


def step_5(r_k_next, r_k):
    num = np.dot(r_k_next, np.transpose(r_k_next))
    den = np.dot(r_k, np.transpose(r_k))
    res = num / den
    print(f"beta_scalar: {num} / {den} = {res}")
    return res


def step_6(r_k_next, b_k_next, p_k):
    res = r_k_next + np.dot(b_k_next, p_k)
    print(f"step_6: {res}")
    return res
