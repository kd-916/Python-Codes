def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = [80, 90, 85, 70, 95]
print(sum_avg(marks))
