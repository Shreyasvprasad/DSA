def trivial_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()  # Use the last element as pivot
    left = []
    right = []

    for num in arr:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return trivial_quicksort(left) + [pivot] + trivial_quicksort(right)

# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = trivial_quicksort(arr)
print("Sorted array (Trivial Quicksort):", sorted_arr)
