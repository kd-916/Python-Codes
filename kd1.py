import random

odd_numbers = [random.randrange(1, 100, 2) for _ in range(5)]
print("Original list of odd numbers:", odd_numbers)

even_numbers = [random.randrange(2, 100, 2) for _ in range(4)]
print("List of even numbers:", even_numbers)

odd_numbers[2] = even_numbers
print("List after replacing third element:", odd_numbers)

flat_list = []
for item in odd_numbers:
    if isinstance(item, list):
        for sub_item in item:
            flat_list.append(sub_item)
    else:
        flat_list.append(item)

flat_list.sort()
print("Flattened and sorted list:", flat_list)
