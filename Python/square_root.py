def square_root(number):
    current_guess = 1

    while current_guess * current_guess <= number:
        current_guess += 1

    return (current_guess - 1)

