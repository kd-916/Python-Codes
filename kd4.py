text = input("Enter a string: ")

char_freq = {}

for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

print("Character frequency:", char_freq)
