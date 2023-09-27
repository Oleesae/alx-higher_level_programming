#!/bin/bash/python3
def magic_calculation(a, b):
    """Computes the power-divided sum of a and b over the range of 1 to 3

    Args:
    a: A float
    b: A float

    Returns:
    A float
    """

    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception:
            result = a + b
            break
    return (result)
