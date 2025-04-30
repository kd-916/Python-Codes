def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

def average(lst):
    if not lst:
        return 0
    return sum_list(lst) / len(lst)

numbers = [4, 8, 15, 16, 23, 42]
print("Average:", average(numbers))
