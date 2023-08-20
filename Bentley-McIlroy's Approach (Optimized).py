def bentley_mcilroy_quicksort(arr, low, high):
    if high <= low:
        return

    if high <= low + 10:  # Use insertion sort for small subarrays
        insertion_sort(arr, low, high)
        return

    lt = low
    gt = high
    v = arr[low]
    i = low + 1

    while i <= gt:
        if arr[i] < v:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > v:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    bentley_mcilroy_quicksort(arr, low, lt - 1)
    bentley_mcilroy_quicksort(arr, gt + 1, high)

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        j = i
        while j > low and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

# Example usage
arr = [12, 11, 13, 5, 6, 7]
bentley_mcilroy_quicksort(arr, 0, len(arr) - 1)
print("Sorted array (Bentley-McIlroy Quicksort):", arr)
