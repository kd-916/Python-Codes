tuples_list = [(1, 2), (), (3, 4), (), (5, 6)]

filtered_list = [tup for tup in tuples_list if tup]

print("List after removing empty tuples:", filtered_list)
