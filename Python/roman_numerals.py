from typing import Tuple

def roman(number: int) -> str:
    VALUE_TO_SYMBOL_LIST = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = []
    remainder = number

    for value, symbol in VALUE_TO_SYMBOL_LIST:
        while remainder >= value:
            result.append(symbol)
            remainder -= value

    return "".join(result)
