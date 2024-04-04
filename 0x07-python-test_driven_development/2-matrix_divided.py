def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number (integer or float).
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if each row of the matrix has the same size
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
