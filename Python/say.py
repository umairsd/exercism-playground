def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"
    chunks = break_into_groups(number)
    if len(chunks) > 4:
        raise ValueError("Number must be less than 999,999,999,999")

    segments = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue

        current = convert_three_digit_number(chunk)

        # words.append(convert_three_digit_number(chunk))
        if i == 1:
            current += " thousand"
        elif i == 2:
            current += " million"
        elif i == 3:
            current += " billion"

        segments.append(current)

    segments.reverse()
    return " ".join(segments)


def convert_three_digit_number(number):
    if number < 0 or number > 999:
        raise ValueError("Number must be between 0 and 999")

    words = []
    hundred_place_digit = number // 100
    if hundred_place_digit > 0:
        words.append(less_than_twenty[hundred_place_digit])
        words.append("hundred")

    two_digit_number = number % 100
    if two_digit_number > 0:
        words.append(convert_less_than_hundred(two_digit_number))

    return " ".join(words)


def convert_less_than_hundred(number):
    if number <= 0 or number >= 100:
        ValueError("Number must be between 0 and 99")

    if number == 0:
        return ""
    elif number % 10 == 0:
        return multiples_of_ten[number]
    elif number < 20:
        return less_than_twenty[number]
    else:
        tens = number // 10  # Won't be 0, as numbers less than 10 are handled.
        units = number % 10  # Won't be 0, as multiples of 10 are handled above.
        return f"{multiples_of_ten[tens * 10]}-{less_than_twenty[units]}"


def break_into_groups(number):
    if number <= 0:
        raise ValueError("Number must be greater than zero.")
    groups = []
    while number > 0:
        groups.append(number % 1000)
        number //= 1000
    return groups


multiples_of_ten = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

less_than_twenty = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

# print(say(0))
# print(say(1))
print(say(1234567890))
print(say(987654321123))
