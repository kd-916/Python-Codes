def count_alpha_digits(s):
    return {"alphabets": sum(1 for c in s if c.isalpha()), "digits": sum(1 for c in s if c.isdigit())}

print(count_alpha_digits("Python123 is fun! 2024"))
