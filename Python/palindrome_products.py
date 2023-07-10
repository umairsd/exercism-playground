def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    for x in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        if is_palindrome(x):
            factors_list = factors_in_range(
                x, range(max_factor, min_factor - 1, -1))
            # As soon as a we find a palindrome with factors, return it
            if factors_list:
                return (x, factors_list)

    return (None, [])


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if max_factor < min_factor:
        raise ValueError("min must be <= max")

    for x in range(min_factor ** 2, (max_factor+1) ** 2):
        if is_palindrome(x):
            factors_list = factors_in_range(
                x, range(min_factor, max_factor + 1))
            # As soon as a we find a palindrome with factors, return it
            if factors_list:
                return (x, factors_list)

    return (None, [])


def factors_in_range(number, number_range):
    """Find the factors of a number in a given range.

    :param number: int
    :param number_range: range
    :return: list of tuples
    """
    factors_list = []
    for f in number_range:
        if number % f == 0 and number // f in number_range:
            factors_list.append((f, number // f))
    return factors_list


def is_palindrome(number):
    """Determine if a number is a palindrome.

    :param number: int
    :return: bool
    """
    return str(number) == str(number)[::-1]
