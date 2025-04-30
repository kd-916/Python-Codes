import random

numbers = {random.randrange(15, 46) for _ in range(10)}
print("Generated set:", numbers)

count_less_than_30 = sum(1 for num in numbers if num < 30)
print("Numbers less than 30:", count_less_than_30)

numbers = {num for num in numbers if num <= 35}
print("Set after removing numbers greater than 35:", numbers)
