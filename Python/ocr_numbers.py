import itertools

mapping = {
    '   \n'
    '  |\n'
    '  |\n'
    '   ': 1,

    ' _ \n'
    ' _|\n'
    '|_ \n'
    '   ': 2,

    ' _ \n'
    ' _|\n'
    ' _|\n'
    '   ': 3,

    '   \n'
    '|_|\n'
    '  |\n'
    '   ': 4,

    ' _ \n'
    '|_ \n'
    ' _|\n'
    '   ': 5,

    ' _ \n'
    '|_ \n'
    '|_|\n'
    '   ': 6,

    ' _ \n'
    '  |\n'
    '  |\n'
    '   ': 7,

    ' _ \n'
    '|_|\n'
    '|_|\n'
    '   ': 8,

    ' _ \n'
    '|_|\n'
    ' _|\n'
    '   ': 9,

    ' _ \n'
    '| |\n'
    '|_|\n'
    '   ': 0,

}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    chunks = split_into_chunks(input_grid, 4)
    result = []
    for chunk in chunks:
        result_line = ''
        for cell in split_into_cells(chunk):
            key = cell_to_string(cell)
            value = mapping.get(key, '?')
            result_line += str(value)
        result.append(result_line)
    return ','.join(result)


def cell_to_string(cell):
    result = '\n'.join(cell)
    return result


def split_into_cells(chunk):
    result = []

    for i in range(0, len(chunk[0]), 3):
        item = []
        for row in chunk:
            item.append(row[i: i + 3])
        result.append(item)
    return result


def split_into_chunks(input_grid, n):
    for i in range(0, len(input_grid), n):
        yield input_grid[i: (i + n)]


bravo = [
    "    _  _ ",
    "  | _| _|",
    "  ||_  _|",
    "         ",
    "    _  _ ",
    "|_||_ |_ ",
    "  | _||_|",
    "         ",
    " _  _  _ ",
    "  ||_||_|",
    "  ||_| _|",
    "         ",
]

charlie = [
    "    _  _     _  _  _  _  _  _ ",
    "  | _| _||_||_ |_   ||_||_|| |",
    "  ||_  _|  | _||_|  ||_| _||_|",
    "                              ",
]

# for chunk in split_into_chunks(bravo, 4):
#     cells = split_into_cells(chunk)
#
#     for line in chunk:
#         print(line)

# for key in mapping:
#     print(key)
#     print(mapping[key])
#     print("xxxxx")

print(convert(charlie))
