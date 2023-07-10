def annotate(minefield):
    # Function body starts here
    num_rows = len(minefield)
    if num_rows == 0:
        return []

    num_columns = len(minefield[0])
    if not is_minefield_valid(minefield):
        raise ValueError("The board is invalid with current input.")

    result = [row[:] for row in minefield]

    for r in range(0, num_rows):
        new_row = ''
        for c in range(0, num_columns):
            if minefield[r][c] == '*':
                new_row += '*'
            else:
                neighboring_values = get_neighboring_values(minefield, r, c)
                neighboring_mines_count = neighboring_values.count('*')
                if neighboring_mines_count == 0:
                    new_row += ' '
                else:
                    new_row += f'{neighboring_mines_count}'
        result[r] = new_row

    return result


def get_neighboring_values(minefield, row, column):
    num_rows = len(minefield)
    if row < 0 or row >= num_rows:
        raise ValueError('Row is out of bounds')

    num_columns = len(minefield[0])
    if column < 0 or column >= num_columns:
        raise ValueError('Column is out of bounds')

    neighbor_indices = [(row, column - 1),
                        (row, column + 1),
                        (row - 1, column),
                        (row - 1, column - 1),
                        (row - 1, column + 1),
                        (row + 1, column),
                        (row + 1, column - 1),
                        (row + 1, column + 1)]

    valid_rows = filter(lambda t: 0 <= t[0] < num_rows, neighbor_indices)
    valid_indices = filter(lambda t: 0 <= t[1] < num_columns, valid_rows)

    neighboring_values = [minefield[t[0]][t[1]] for t in valid_indices]
    return neighboring_values


def is_minefield_valid(minefield):
    num_columns = len(minefield[0])
    if any(len(row) != num_columns for row in minefield):
        return False

    for row in minefield:
        if any((e != ' ' and e != '*') for e in row):
            return False

    return True
