def dijkstra_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Use the middle element as pivot
    left = []
    equal = []
    right = []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    return dijkstra_quicksort(left) + equal + dijkstra_quicksort(right)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = dijkstra_quicksort(arr)
print("Sorted array (Dijkstra's Quicksort):", sorted_arr)
