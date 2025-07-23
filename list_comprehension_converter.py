# Convert traditional for-loop-based list creation into list comprehensions. Include examples with:

# Simple list creation
# Filtering conditions (e.g., only even numbers)
# Nested loops (e.g., combinations or matrix flattening)


square = []
for i in range(1, 11):
    square.append(i * i)
print(square)

square = [i * i for i in range(1, 11)]
print(square)

even = []
for i in range(1, 11):
    if i % 2 == 0:
        even.append(i)
print(even)

even = [i for i in range(1, 11) if i % 2 == 0]
print(even)
