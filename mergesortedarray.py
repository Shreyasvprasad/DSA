def merge_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = []
    i = j = 0

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # Append remaining elements from both arrays, if any
    while i < n1:
        merged.append(arr1[i])
        i += 1
    
    while j < n2:
        merged.append(arr2[j])
        j += 1
    
    return merged

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge_sorted_arrays(arr1, arr2)
print("Merged sorted array:", result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
