# Write a one-liner Python code to generate a list of squares of even numbers from 1 to 10.

squares_of_even_numbers = [i*i for i in range(1, 11) if i % 2 == 0]
print(squares_of_even_numbers)

# Write a one-liner Python code to capitalize the first letter of each word in a list of strings.

capitalized_words = list(map(str.capitalize, ['hello', 'world']))
print(capitalized_words)

# Write a one-liner Python code to find the maximum value in a list of numbers.

max_value = max(1, 2, 3, 4, 5)
print(max_value)

# Write a one-liner Python code to find the sum of a list of numbers.

from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(sum_of_numbers)
