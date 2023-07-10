
def flatten(iterable):
    result = []
    try:
        concrete_iterable = iter(iterable)
        for item in concrete_iterable:
            result += flatten(item)
        return result
    except TypeError:
        if iterable is not None:
            return [iterable]
        else:
            return []


print(flatten([1,[2,3,None,4],[None],5]))