#!/usr/bin/python3
"""
matrix_divided

list of lists, num -> list of numbers

"""


def matrix_divided(matrix, div):
    """ (list, number) -> list

    Return list of matrix divided by div
    matrix is a list of lists of equal lengths.
    div is a number

    Precondition: div > 0
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list")
    if not all(isinstance(elem, list) for elem in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for elem in matrix:
        for num in elem:
            if not isinstance(num, (float, int)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix)-1):
        if len(matrix[i]) != len(matrix[i+1]):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        return [[round(num/div, 2) for num in elem] for elem in matrix]
