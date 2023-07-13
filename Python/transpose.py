import itertools
from typing import List


def transpose(text: str) -> str:
    if '\n' not in text:
        return '\n'.join(list(text))

    lines = text.replace(' ', '^').splitlines()
    # Zip each line. Wherever there are gaps, it uses ` ` to fill them.
    tuples = itertools.zip_longest(*lines, fillvalue=' ')
    result = []
    for t in tuples:
        joined_str = "".join(t).rstrip()
        result.append(joined_str)
    transposed = '\n'.join(result)
    # restore pre-existing spaces
    return transposed.replace("^", " ")


def transpose_(lines: str) -> str:
    rows = lines.split('\n')

    max_length = max([len(x) for x in rows], default=0)
    padded_lines = pad_lines(rows, max_length)

    result = []
    for column in range(0, max_length):
        value = ''
        for line in padded_lines:
            if column < len(line):
                value += line[column]

        result.append(value)
    return '\n'.join(result)


def pad_lines(lines: List[str], max_length: int) -> List[str]:
    result = []
    for line in lines[:-1]:
        padding_length = max_length - len(line)
        padding = ' ' * padding_length
        result.append(line + padding)
    result.append(lines[-1])
    return result


print(transpose('\n'.join([])))
print('\n')
print(transpose('\n'.join(["A1"])))
print('\n')
print(transpose('\n'.join(["A", "1"])))
print('\n')
print(transpose('\n'.join(["ABC", "123"])))
print('\n')
print(transpose('\n'.join(["HEART", "EMBER", "ABUSE", "RESIN", "TREND"])))
print('\n')
print(transpose('\n'.join(["The fourth line.", "The fifth line."])))
print('\n')
# expected = [
#     "TT",
#     "hh",
#     "ee",
#     "  ",
#     "ff",
#     "oi",
#     "uf",
#     "rt",
#     "th",
#     "h ",
#     " l",
#     "li",
#     "in",
#     "ne",
#     "e.",
#     ".",
# ]
# print("\n".join(expected))
print('\n')
print(transpose('\n'.join(["Single line."])))
print('\n')
print(transpose('\n'.join(["The longest line.", "A long line.", "A longer line.", "A line."])))
print('\n')
