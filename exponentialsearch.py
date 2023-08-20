def exponential_search(arr, target):
    n = len(arr)
    if arr[0] == target:
        return 0
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n - 1))

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 9
result = exponential_search(arr, target)
print("Exponential Search Result:", result)
