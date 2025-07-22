from functools import reduce

square = lambda x: x * x
print(square(5))

reverse = lambda x: x[::-1]
print(reverse("hello"))

filter_evens = lambda x: list(filter(lambda x: x % 2 == 0, x))
print(filter_evens([1, 2, 3, 4, 5]))

sum_of_list = lambda x: sum(x)
print(sum_of_list([1, 2, 3, 4, 5]))

factorial = lambda x: reduce(lambda x, y: x * y, range(1, x + 1))
print(factorial(5))

