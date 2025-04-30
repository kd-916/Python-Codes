import random

numbers = [random.randrange(-50, 51) for _ in range(30)]
print("Generated list:", numbers)

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
