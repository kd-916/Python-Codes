foods = [("Burger", 150), ("Pizza", 300), ("Pasta", 200), ("Fries", 100)]

foods.sort(key=lambda x: x[1], reverse=True)

print("Sorted food items:", foods)
