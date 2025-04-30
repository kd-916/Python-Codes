def count_lower_upper(s):
    result = {"lowercase": sum(1 for c in s if c.islower()), "uppercase": sum(1 for c in s if c.isupper())}
    return result

sample_string = "Hello World! This is Python."
print(count_lower_upper(sample_string))
