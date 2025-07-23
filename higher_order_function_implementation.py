def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

print(custom_map(lambda x: x * 2, [1, 2, 3, 4, 5]))

def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

def custom_reduce(func, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = func(result, item)
    return result

print(custom_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
