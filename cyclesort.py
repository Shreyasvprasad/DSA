def cycle_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        item = arr[i]
        pos = i
        for j in range(i + 1, n):
            if arr[j] < item:
                pos += 1
        
        if pos == i:
            continue
        
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        
        while pos != i:
            pos = i
            for j in range(i + 1, n):
                if arr[j] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
cycle_sort(arr)
print("Sorted array (Cycle Sort):", arr)
