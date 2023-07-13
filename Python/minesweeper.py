def annotate(minefield):
    # Function body starts here
    num_rows = len(minefield)
    if num_rows == 0:
        return []

    num_columns = len(minefield[0])
    if not is_minefield_valid(minefield):
        raise ValueError("The board is invalid with current input.")

    result = []
    for r, row in enumerate(minefield):
        new_row = ""
        for c, elem in enumerate(row):
            if elem == "*":
                new_row += "*"
            else:
                mine_count = get_neighboring_mine_count(minefield, r, c)
                new_row += (
                    str(mine_count)
                    if mine_count != 0
                    else " "
                )
        result.append(new_row)
    return result


def get_neighboring_mine_count(minefield, row, column):
    return len(
        [
            1
            for ir in [-1, 0, 1]
            for ic in [-1, 0, 1]
            if not (
                (ic == 0 and ir == 0)
                or (row + ir < 0)
                or (row + ir >= len(minefield))
                or (column + ic < 0)
                or (column + ic >= len(minefield[0]))
            )
            and minefield[row + ir][column + ic] == "*"
        ])


def is_minefield_valid(minefield):
    num_columns = len(minefield[0])
    if any(len(row) != num_columns for row in minefield):
        return False

    if not all(all((e == ' ' or e == '*') for e in row) for row in minefield):
        return False

    return True
