import random

numbers = [random.randint(1, 50) for _ in range(20)]
print("Generated list:", numbers)

user_num = int(input("Enter a number: "))

positions = [i for i, num in enumerate(numbers) if num == user_num]

print("Positions:", positions if positions else "Number not found")
