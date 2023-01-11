#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(matrix[row][i]), end='')
        print()
