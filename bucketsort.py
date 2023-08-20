def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / len(arr)
    n = len(arr)
    
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)
    
    for i in range(n):
        insertion_sort(buckets[i])  # Apply insertion sort within each bucket
    
    k = 0
    for i in range(n):
        for num in buckets[i]:
            arr[k] = num
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
bucket_sort(arr)
print("Sorted array (Bucket Sort):", arr)
