def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# Example usage
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
result = interpolation_search(arr, target)
print("Interpolation Search Result:", result)
