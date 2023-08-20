def count_set_bits(num):
    count = 0
    while num > 0:
        count += num & 1
        num >>= 1
    return count

def custom_compare(x):
    return (-count_set_bits(x), x)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if custom_compare(left[i]) <= custom_compare(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage
arr = [5, 2, 8, 10, 12]
sorted_arr = merge_sort(arr)
print("Sorted array based on count of set bits:", sorted_arr)
