#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row[element]**2 for element in range(len(row))] for row in matrix]
