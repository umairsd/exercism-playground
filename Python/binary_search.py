def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if search_list[mid] == value:
            return mid

        if search_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")


print(find([6], 6))
print(f"{find([1, 3, 4, 6, 8, 9, 11], 6)} - Expected 3")
print(f"{find([6], 6)} - Expected 0")
print(f"{find([1, 3, 4, 6, 8, 9, 11], 6)} - Expected 3")
print(f"{find([1, 3, 4, 6, 8, 9, 11], 1)} - Expected 0")
print(f"{find([1, 3, 4, 6, 8, 9, 11], 11)} - Expected 6")
print(f"{find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144)} - Expected 9")
print(f"{find([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21)} - Expected 5")
