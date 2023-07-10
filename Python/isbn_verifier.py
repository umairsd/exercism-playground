def is_valid(isbn):
    total = 0
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    countX = isbn.count('X')
    if countX > 1 or (countX == 1 and isbn[-1] != 'X'):
        return False

    for i, d in enumerate(isbn):
        multiplier = 10 - i

        if d.isdigit():
            total += multiplier * int(d)
        elif d == 'X':
            total += 10
        else:
            return False

    return total % 11 == 0


print(is_valid("3-598-21508-8"))