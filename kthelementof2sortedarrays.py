def find_kth_element(arr1, arr2, k):
    n, m = len(arr1), len(arr2)
    i, j = 0, 0
    kth_element = None
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            kth_element = arr1[i]
            i += 1
        else:
            kth_element = arr2[j]
            j += 1
        
        k -= 1
        if k == 0:
            return kth_element
    
    while i < n and k > 0:
        kth_element = arr1[i]
        i += 1
        k -= 1
    
    while j < m and k > 0:
        kth_element = arr2[j]
        j += 1
        k -= 1
    
    return kth_element

# Example usage
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
result = find_kth_element(arr1, arr2, k)
print("Element at kth position:", result)  # Output: 6
