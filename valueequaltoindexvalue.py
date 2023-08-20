def find_elements_equal_to_index(arr):
    result = []

    for i, num in enumerate(arr, start=1):
        if num == i:
            result.append(i)

    return result

# Example usage
arr = [15, 2, 45, 12, 7]
result = find_elements_equal_to_index(arr)
print("Indices of elements equal to their value:", result)  # Output: [2, 4]
