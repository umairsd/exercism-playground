color_values = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors):
    number = value(colors)
    (divisor, suffix) = divisor_suffix(number)
    return f"{number // divisor} {suffix}"


def value(colors):
    number_of_zeros = color_values[colors[2]]
    number = color_values[colors[0]] * 10 + color_values[colors[1]]
    number = number * (10 ** number_of_zeros)
    return number


def divisor_suffix(number):
    if number >= 10 ** 9:
        return 10 ** 9, "gigaohms"
    elif number >= 10 ** 6:
        return 10 ** 6, "megaohms"
    elif number >= 10 ** 3:
        return 10 ** 3, "kiloohms"
    else:
        return 1, "ohms"


print(label(["orange", "orange", "black"]))
