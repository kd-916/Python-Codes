def frequency(s):
    words = s.split()
    return {word: words.count(word) for word in sorted(set(words))}

print(frequency("apple banana apple orange banana apple"))
