import random

nums = [random.randint(-15, 15) for _ in range(10)]
squares = list(map(lambda x: x**2, nums))

print("Original:", nums)
print("Squares:", squares)

