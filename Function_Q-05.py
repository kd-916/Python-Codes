def ispangram(s):
    return set("abcdefghijklmnopqrstuvwxyz") <= set(s.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
