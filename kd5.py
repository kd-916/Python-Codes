names = ["Dr. Anil", "Samantha", "Jonathan", "Priya", "Christopher"]

long_names = list(filter(lambda name: len(name) > 8, names))

print("Names longer than 8 characters:", long_names)
