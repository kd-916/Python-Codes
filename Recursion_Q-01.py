def to_binary(n):
    if n == 0:
        return ""
    return to_binary(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))
print("Binary equivalent:", to_binary(num) or "0")
