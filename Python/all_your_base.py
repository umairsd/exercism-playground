def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(digit < 0 or digit >= input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert to base 10
    base10 = 0
    for digit in digits:
        base10 = base10 * input_base + digit

    if base10 == 0:
        return [0]

    # Convert to output base.
    output_digits = []
    number = base10
    while number > 0:
        d = number % output_base
        output_digits.append(d)
        number = number // output_base

    output_digits.reverse()
    return output_digits
