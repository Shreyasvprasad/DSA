def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    left = arr[l : l + n1]
    right = arr[m + 1 : m + 1 + n2]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

def bottom_up_merge_sort(arr):
    n = len(arr)
    curr_size = 1
    
    while curr_size < n - 1:
        left = 0
        
        while left < n - 1:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            merge(arr, left, mid, right)
            left += 2 * curr_size
        curr_size *= 2

# Example usage
arr = [12, 11, 13, 5, 6, 7]
bottom_up_merge_sort(arr)
print("Sorted array:", arr)
