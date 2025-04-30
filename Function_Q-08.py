def convert(s):
    return " ".join(sorted(set(s.split())))

print(convert("apple banana apple orange banana mango"))
