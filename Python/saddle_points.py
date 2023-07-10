def saddle_points(matrix):
    if len(matrix) is 0:
        return []

    if is_irregular(matrix):
        raise ValueError("irregular matrix")

    max_row_values = max_row_elements(matrix)
    min_column_values = min_column_elements(matrix)
    result = []

    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):
            value = matrix[r][c]
            if max_row_values[r] <= value <= min_column_values[c]:
                sp = {"row": r + 1, "column": c + 1}
                result.append(sp)
                # result.append((r + 1, c + 1))

    return result


# Returns an array equal to the number of rows.
def max_row_elements(matrix):
    result = []
    for row in matrix:
        result.append(max(row))
    return result


# Returns an array equal to the number of columns.
def min_column_elements(matrix):
    result = []

    for c in range(0, len(matrix[0])):
        max_value = 1_000_000
        for r in range(0, len(matrix)):
            max_value = min(max_value, matrix[r][c])

        result.append(max_value)

    return result


def is_irregular(matrix):
    column_width = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != column_width:
            return True
    return False


print(saddle_points([]))
m = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
print(saddle_points(m))
