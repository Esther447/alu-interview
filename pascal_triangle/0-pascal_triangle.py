#!/usr/bin/python3
"""
0-pascal_triangle
Generates Pascal’s Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Returns a list ofty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # First element is always 1
        for j in range(1, i):
            # Add two numbers from the previous row
            row.append(
                prev_row[j - 1] + prev_row[j]
            )
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
