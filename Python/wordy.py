supported_ops = ['plus', 'minus', 'multiplied', 'divided']


def answer(question):
    words = question[:-1].split()
    words = [w for w in words[2:] if w not in ['by']]
    if len(words) == 0:
        raise ValueError("syntax error")

    if len(words) == 1 and maybe_int(words[0]) is not None:
        return int(words[0])

    # words at odd index.
    operators = words[1::2]
    # Conditions:
    # - Every alternate word starting from the 1st index should be a word,
    # - Each of these must be a supported operator.
    if any([not x.isalpha() for x in operators]):
        raise ValueError("syntax error")
    if [x for x in operators if x not in supported_ops]:
        raise ValueError("unknown operation")

    # words at even index.
    operands = words[::2]
    int_operands = [int(x) for x in operands if maybe_int(x) is not None]
    # Conditions:
    # - Every alternate word starting from the 0th index should be an integer.
    # - If no operands, unknown operation.
    # - If only one operand, syntax error.
    # there should be at least 2 integers.
    if not int_operands:
        raise ValueError("unknown operation")
    if len(int_operands) != len(operands):
        raise ValueError("syntax error")
    if len(int_operands) == 1:
        raise ValueError("syntax error")

    current_op_index = 0
    left_num = int_operands[0]
    for i in range(1, len(operands)):
        right_num = int_operands[i]
        if operators[current_op_index] == 'plus':
            left_num += right_num
        elif operators[current_op_index] == 'minus':
            left_num -= right_num
        elif operators[current_op_index] == 'multiplied':
            left_num *= right_num
        elif operators[current_op_index] == 'divided':
            left_num /= right_num
        else:
            raise ValueError("unknown operation")

        current_op_index += 1

    return left_num


def maybe_int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None
