from typing import Callable, List
from typing import TypeVar

T = TypeVar('T')
S = TypeVar('S')
U = TypeVar('U')

def _append(list1: List[T], list2: List[T]) -> List[T]:
    return [*list1, *list2]


def _concat(list_of_lists: List[List[T]]) -> List[T]:
    result: List[T] = []
    for l in list_of_lists:
        result = _append(result, l)
    return result


def _filter(function: Callable[[T], bool], items: List[T]) -> List[T]:
    return [e for e in items if function(e)]


def _length(items: List[T]) -> int:
    count = 0
    for item in items:
        count += 1
    return count


def _map(function: Callable[[T], S], items: List[T]) -> List[S]:
    return [function(e) for e in items]


def _foldl(function: Callable[[U, T], U], items: List[T], initial: U) -> U:
    result = initial
    for item in items:
        result = function(result, item)
    return result


def _foldr(function: Callable[[U, T], U], items: List[T], initial: U) -> U:
    result = initial
    for item in _reverse(items):
        result = function(result, item)
    return result

def _reverse(items: List[T]) -> List[T]:
    return items[::-1]


