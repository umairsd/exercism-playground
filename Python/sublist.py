"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 0
UNEQUAL = 2


def sublist(list_one, list_two):
    len1 = len(list_one)
    len2 = len(list_two)
    if len1 == len2 and list_one == list_two:
        return EQUAL
    elif len1 < len2 and is_sublist(list_one, list_two):
        return SUBLIST
    elif len1 > len2 and is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL


def is_sublist(list_one, list_two):
    len1 = len(list_one)
    len2 = len(list_two)

    if len1 > len2:
        return False

    # go from 0 to (len2 - len1 + 1) to check all possible starting points.
    for i in range(len2 - len1 + 1):
        if list_one == list_two[i : i + len1]:
            return True

    return False
