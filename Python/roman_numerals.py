from typing import Tuple

def roman(number: int) -> str:
    result = []

    while number > 0:
        if number >= 1000:
            result.append("M" * (number // 1000))
            number %= 1000

        elif number >= 900:
            result.append("CM")
            number %= 900

        elif number >= 500:
            result.append("D")
            number %= 500

        elif number >= 400:
            result.append("CD")
            number %= 400

        elif number >= 100:
            result.append("C" * (number // 100))
            number %= 100

        elif number >= 90:
            result.append("XC")
            number %= 90

        elif number >= 50:
            result.append("L")
            number %= 50

        elif number >= 40:
            result.append("XL")
            number %= 40

        elif number >= 10:
            result.append("X" * (number // 10))
            number %= 10

        elif number >= 9:
            result.append("IX")
            number %= 9

        elif number >= 5:
            result.append("V")
            number %= 5

        elif number >= 4:
            result.append("IV")
            number %= 4

        else:
            result.append("I" * number)
            number %= 1

    return "".join(result)


# def roman(partial_number: int, current: str) -> Tuple[int, str]:
#     if number
#     if partial_number > 1000:
#         partial_number %- 1000
#         partial_number.append
print(roman(93))