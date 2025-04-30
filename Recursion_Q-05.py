def sanitize_list(lst):
    if not lst:
        return []
    return [0 if lst[0] < 0 else lst[0]] + sanitize_list(lst[1:])

values = [5, -3, 7, -1, 0, -9]
print("Sanitized list:", sanitize_list(values))
