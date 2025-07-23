#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    matrix_len = len(matrix)
    for i in range(matrix_len):
        new_matrix.append(list(map(lambda x: x * x, matrix[i])))
    return new_matrix
