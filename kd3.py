names = set()

names.update(["Alice", "Bob", "Charlie", "David", "Emma"])
print("Set after adding names:", names)

names.discard("Charlie")
names.add("Charlotte")
print("Set after modifying a name:", names)

names.discard("Bob")
names.discard("Emma")
print("Set after deleting two names:", names)
