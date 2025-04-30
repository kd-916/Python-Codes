students = [(101, "Alice", 20), (102, "Bob", 22), (103, "Charlie", 21)]

roll_numbers = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", roll_numbers)
print("Names:", names)
print("Ages:", ages)
