#!/usr/bin/python3
# 2-matrix_divided.py

def matrix_divided(matrix, div):
    """Divides all element of matrix

    Raises:
    TypeError: must be list of lists of integers and floats
    TypeError: row of matrix must be same size
    TypeError: div must be number
    ZeroDivisionError: div cann't be zero
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("marix must be a matrix(list of lists) of"
                "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("Division by Zero")
    return ([list(map(lambda x: round(x/div, 2), row)) for row in matrix])
