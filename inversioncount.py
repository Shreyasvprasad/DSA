"""Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Implement a modified merge sort function that takes the array arr, a starting index start, an ending index end, and an auxiliary array temp for merging.

Divide the array into two halves recursively until the array size becomes 1.

During the merge step, while merging the two sorted halves, count the number of inversions by comparing elements from both halves.

If arr[i] from the first half is greater than arr[j] from the second half, it means there are mid - i + 1 inversions with arr[j] and all the elements to its left in the first half.
After merging the two halves, return the inversion count"""
def mergeSort(arr, start, end, temp):
    inv_count = 0

    if start < end:
        mid = (start + end) // 2

        # Divide the array into two halves and recursively sort them
        inv_count += mergeSort(arr, start, mid, temp)
        inv_count += mergeSort(arr, mid + 1, end, temp)

        # Merge the two sorted halves and count inversions
        inv_count += merge(arr, start, mid, end, temp)

    return inv_count

def merge(arr, start, mid, end, temp):
    inv_count = 0

    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += (mid - i + 1)  # Count inversions

        k += 1

    # Copy the remaining elements from the first half
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements from the second half
    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the merged elements back to the original array
    for i in range(start, end + 1):
        arr[i] = temp[i]

    return inv_count

def inversionCount(arr):
    n = len(arr)
    temp = [0] * n  # Auxiliary array for merging
    return mergeSort(arr, 0, n - 1, temp)
