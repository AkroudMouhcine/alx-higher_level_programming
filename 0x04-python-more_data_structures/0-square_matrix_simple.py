#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row[element_index]**2 for element_index in range(len(row))] for row in matrix] 
