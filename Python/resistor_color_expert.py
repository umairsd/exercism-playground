resistor_color_value_map = {
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

tolerance_map = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors):
    # <= 2: simply generate value.
    colors_count = len(colors)

    if colors_count <= 2:
        resistor_value = build_resistor_value(colors)
        return f"{resistor_value} ohms"
    elif colors_count == 3:
        multiplier_value = resistor_color_value_map[colors[-1]]
        multiplier = 10 ** multiplier_value
        resistor_value = build_resistor_value(colors[:-1], multiplier)
        return f"{resistor_value} ohms"
    else:
        tolerance = tolerance_map[colors[-1]]
        multiplier_value = resistor_color_value_map[colors[-2]]
        multiplier = 10 ** multiplier_value
        resistor_value = build_resistor_value(colors[:-2], multiplier)
        return resistor_value_str(resistor_value, tolerance)
    pass


def resistor_value_str(resistor_value, tolerance):
    (divisor, suffix) = divisor_suffix(resistor_value)

    result = resistor_value // divisor
    remainder = resistor_value % divisor

    if remainder == 0:
        return f"{result} {suffix} ±{tolerance}%"
    else:
        return f"{resistor_value / divisor} {suffix} ±{tolerance}%"


def build_resistor_value(colors, multiplier=1):
    if len(colors) > 3:
        raise ValueError("Incorrect size of the array")

    number = 0
    for c in colors:
        v = resistor_color_value_map[c]
        number *= 10
        number += v

    number *= multiplier
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


print(resistor_label(["brown", "red", "orange", "green", "blue"]))
print(resistor_label(["blue", "grey", "brown", "violet"]))
