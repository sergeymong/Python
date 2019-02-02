from functools import reduce
import cProfile
from functools import partial


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


# its the same that reduce
# def vector_sum(*vectors):
#     resul# t = vectors[0]
#
#     for vector in vectors[1:]:
#         result = vector_add(result, vector)
#
#     return result


def vector_sum(*vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


def vector_mean(*vectors):
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


# scalar multiply
def dot(v, w):
    """v1 * w1 + v2 * w2 ... + vn * wn"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v1 * v1 + ... vn * vn"""
    return dot(v, v)


def magnitude(v):
    from math import sqrt
    return sqrt(sum_of_squares(v))


def squared_distance(v, w):
    """"(v1 - w2) ** 2 + ... + (vn - wn) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


# distance between two vectors
def distance(v, w):
    return magnitude(vector_subtract(v, w))


##################
# matrix functions
##################

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_columns(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)

print(identity_matrix)
#  x = range(10000)
#  y = range(50000, 60000)
#
#  print(distance(x, y))
