employees = {
    "HR": [(101, 50000), (102, 55000)],
    "IT": [(201, 70000), (202, 75000)],
    "Sales": [(301, 40000), (302, 45000)]
}

for dept, records in employees.items():
    salaries = [salary for _, salary in records]
    print(f"{dept} - Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")
