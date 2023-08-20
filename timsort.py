from sortedcontainers import SortedList

def tim_sort(arr):
    sorted_list = SortedList(arr)
    sorted_arr = [x for x in sorted_list]

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
tim_sort(arr)
print("Sorted array (Tim Sort):", arr)
