import itertools
from typing import Tuple


def encode(message: str, rails: int):
    result = list(itertools.repeat("", rails))
    message = message.replace(" ", "")

    row = 0
    should_increment = True

    for c in message:
        result[row] += c
        row, should_increment = update_to_zig_zag(row, should_increment, rails)

    return "".join(result)


def decode(encoded_message, rails):
    matrix = [["." for _ in range(len(encoded_message))] for _ in range(rails)]

    # mark the places with '*'
    row, column = 0, 0
    should_increment = True
    for _ in encoded_message:
        matrix[row][column] = "*"
        column += 1

        row, should_increment = update_to_zig_zag(row, should_increment, rails)

    # Replace the "*" positions with the correct letter.
    index = 0
    for r in range(rails):
        for c in range(len(encoded_message)):
            if matrix[r][c] == "*" and index < len(encoded_message):
                matrix[r][c] = encoded_message[index]
                index += 1

    # Now, read the matrix in a zig-zag manner.
    result = []
    should_increment = True
    row, column = 0, 0
    for _ in encoded_message:
        if matrix[row][column] != ".":
            result.append(matrix[row][column])
            column += 1
        row, should_increment = update_to_zig_zag(row, should_increment, rails)

    return "".join(result)


def update_to_zig_zag(row: int, should_increment: bool, levels: int)\
      -> Tuple[int, bool]:
    if should_increment:
        row += 1
        should_increment = (row != levels - 1)
    else:
        row -= 1
        should_increment = (row == 0)

    return row, should_increment
