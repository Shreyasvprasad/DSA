"""Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array."""
"""Dutch National Flag algorithm.
Initialize three pointers, low = 0, mid = 0, and high = n - 1.

Iterate through the array while mid <= high:

If arr[mid] is less than a, swap arr[mid] with arr[low], increment low and mid by 1.

If arr[mid] is between a and b, increment mid by 1.

If arr[mid] is greater than b, swap arr[mid] with arr[high], decrement high by 1.

After the iteration, the array arr will be partitioned around the range [a, b] as required.
"""
def partitionArray(arr, a, b):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] < a:
            arr[mid], arr[low] = arr[low], arr[mid]
            low += 1
            mid += 1
        elif arr[mid] >= a and arr[mid] <= b:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
