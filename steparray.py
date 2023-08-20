def find_first_occurrence(arr, x):
    n = len(arr)
    
    for i in range(n):
        if arr[i] == x:
            return i
    
    return -1  # Return -1 if the key x is not found

# Example usage
arr = [4, 2, 6, 7, 1, 3]
x = 6
result = find_first_occurrence(arr, x)
if result != -1:
    print("First occurrence of", x, "is at index:", result)
else:
    print(x, "not found in the array")
