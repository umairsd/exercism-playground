from typing import Callable
from typing import Any
from typing import TypeVar

T = TypeVar('T')
S = TypeVar('S')
U = TypeVar('U')

def append(list1: [T], list2: [T]) -> [T]:
    for item in list2:
        list1.append(item)
    return list1


def concat(list_of_lists: [[T]]) -> [T]:
    result: [T] = []
    for l in list_of_lists:
        result = append(result, l)
    return result

# def filter(function, items):
def _filter(function: Callable[[T], bool], items: [T]) -> [T]:
    result: [T] = []
    for item in items:
        if function(item):
            result.append(item)
    return result

# def length(items):
def _length(items: [T]) -> int:
    count = 0
    for item in items:
        count += 1
    return count


# def map(function, items):
def _map(function: Callable[[T], S], items: [T]) -> [S]:
    result: [S] = []
    for item in items:
        result.append(function(item))
    return result

# def foldl(function, items, initial):
def _foldl(function: Callable[[U, T], U], items: [T], initial: U) -> U:
    result = initial
    for item in items:
        result = function(result, item)
    return result


# def _foldr(function, items, initial):
def _foldr(function: Callable[[T, U], U], items: [T], initial: U) -> U:
    result = initial
    for item in _reverse(items):
        result = function(item, result)
    return result


def _reverse(items: [T]) -> [T]:
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result


filtered = _filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(filtered)

mapped = _map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(mapped)