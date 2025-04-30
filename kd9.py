list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 4, 7, 8, 9]

unique_numbers = [num for num in list1 if num not in list2]

print("Unique numbers from first list:", unique_numbers)
