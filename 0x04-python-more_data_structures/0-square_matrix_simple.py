#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sequared_matrix = []
    for row in matrix:
        sequared_row = []
        for element in row:
            sequard_element = element ** 2
            sequared_row.append(sequard_element)
        sequared_matrix.append(sequared_row)
    return sequared_matrix
            
