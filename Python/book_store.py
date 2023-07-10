import sys
from collections import Counter

price_of_one_book = 8

discount_percentage = {
    1: 0,
    2: 5,
    3: 10,
    4: 20,
    5: 25
}


def total(basket):
    """Calculates the price of books in the `basket`.

    :param basket: list - a basket of books.
    :return: int - total price of the books.
    """

    min_total_price = sys.maxsize

    tuples = convert_dict_to_list_of_tuples(Counter(basket))
    set_of_length_tuples = set()
    current_list = []
    build_all_sets(tuples, set_of_length_tuples, current_list)

    for combo in set_of_length_tuples:
        total_price = 0
        for set_length in combo:
            price = set_length * price_of_one_book * (
                        100 - discount_percentage.get(set_length, 0))
            total_price += price

        min_total_price = min(total_price, min_total_price)

    return min_total_price


def total_book_count(list_of_tuples):
    books = sum([x[1] for x in list_of_tuples])
    return books


def sort_list_of_tuples(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    return sorted_list


def convert_dict_to_list_of_tuples(book_counts):
    result = []
    for key, value in book_counts.items():
        result.append((key, value))
    return result


def build_all_sets(book_count_tuples, set_of_length_tuples, current_set):
    if total_book_count(book_count_tuples) == 0:
        sorted_lengths = sorted([len(x) for x in current_set])
        lengths_tuple = tuple(sorted_lengths)
        set_of_length_tuples.add(lengths_tuple)
        return

    max_possible = unique_books(book_count_tuples)

    for max_set_length in range(max_possible, 0, -1):
        sorted_tuples = sort_list_of_tuples(book_count_tuples[:])
        book_set = build_largest_set_of_size(sorted_tuples, max_set_length)
        if not book_set:
            continue

        updated_set = current_set[:]
        updated_set.append(book_set)
        # recurse.
        build_all_sets(sorted_tuples, set_of_length_tuples, updated_set)

    return


def unique_books(book_count_tuples):
    books = len([x for x in book_count_tuples if x[1] > 0])
    return books


def build_largest_set_of_size(book_count_tuples, max_size):
    """Chooses the most number of books from the list of books.

    :param max_size:
    :param book_count_tuples: list - a list of tuples (book, book_count).
    :return: set - the largest set of books we can build.
    """
    book_set = set()

    for i in range(0, len(book_count_tuples)):
        entry = book_count_tuples[i]
        book = entry[0]
        book_count = entry[1]
        if book not in book_set and book_count > 0 and len(book_set) < max_size:
            book_set.add(book)
            book_count_tuples[i] = book, book_count - 1

    if len(book_set) == 0:
        return None
    return book_set


# test([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5])
def test(basket):
    tuples = convert_dict_to_list_of_tuples(Counter(basket))
    list_of_sets = []
    current_list = []
    build_all_sets(tuples, list_of_sets, current_list)
    return


# print(f"Expect: 800, Actual: {total([1])}")
# print(f"Expect: 1600, Actual: {total([2, 2])}")
# print(f"Expect: 0, Actual: {total([])}")
# print(f"Expect: 1520, Actual: {total([1, 2])}")
# print()
# print(f"Expect: 2160, Actual: {total([1, 2, 3])}")
# print(f"Expect: 2560, Actual: {total([1, 2, 3, 4])}")
# print(f"Expect: 3000, Actual: {total([1, 2, 3, 4, 5])}")
# print(f"Expect: 5120, Actual: {total([1, 1, 2, 2, 3, 3, 4, 5])}")
# print()
# print(f"Expect: 5120, Actual: {total([1, 1, 2, 3, 4, 4, 5, 5])}")
# print(f"Expect: 4080, Actual: {total([1, 1, 2, 2, 3, 4])}")
# print(f"Expect: 5560, Actual: {total([1, 1, 2, 2, 3, 3, 4, 4, 5])}")
# print(f"Expect: 6000, Actual: {total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])}")
#
# print()
# print(f"Expect: 6800, Actual: {total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1])}")
# print(f"Expect: 7520, Actual: {total([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 1, 2])}")
# print(f"Expect: 10240, "
#       f"Actual: {total([1, 1, 2, 2, 3, 3, 4, 5, 1, 1, 2, 2, 3, 3, 4, 5])}")
#
# print()
# print(f"Expect: 3360, Actual: {total([1, 1, 2, 3, 4])}")
# print(f"Expect: 10000, "
#       f"Actual: {total([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])}")
# print(f"Expect: 8120, "
#       f"Actual: {total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5])}")
# print(f"Expect: 8120, "
#       f"Actual: {total([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3])}")

print(f"Expect: 8120, "
      f"Actual: {total([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5])}")
