#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """Returns a list of lists of numbers
    representing the Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [0] * n

    for i in range(n):
        # Define a row and fill first and last index with 1
        new_row = [0] * (i + 1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = triangle[i - 1][j]
                b = triangle[i - 1][j - 1]
                new_row[j] = a + b

        triangle[i] = new_row

    return triangle
