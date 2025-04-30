import random

numbers = [random.randrange(1, 31) for _ in range(50)]
print("Generated list:", numbers)

unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)
