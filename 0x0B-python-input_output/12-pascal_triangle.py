#!/usr/bin/python3

"""
Returns Pascal's triangle of n.
"""

def pascal_triangle(n):
    """
    Returns Pascal's triangle of n.

    Args:
        n (int): Number of rows for Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element of every row is 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])  # Calculate each element based on the previous row
        new_row.append(1)  # Last element of every row is 1
        triangle.append(new_row)

    return triangle

# Test cases
print(pascal_triangle(5))
