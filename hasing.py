def hashing_search(arr, target):
    hash_table = {}
    for idx, val in enumerate(arr):
        hash_table[val] = idx
    if target in hash_table:
        return hash_table[target]
    return -1

# Example usage
arr = [3, 7, 1, 9, 5]
target = 7
result = hashing_search(arr, target)
print("Hashing Search Result:", result)
