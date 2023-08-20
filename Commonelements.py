"""Given three arrays sorted in increasing order. Find the elements that are common in all three arrays."""
"""Initialize three pointers, i, j, and k, to the start of each array.

Initialize a variable prev to None to keep track of the previously found common element.

Iterate through the arrays until any of the pointers reaches the end of its respective array.

If arr1[i], arr2[j], and arr3[k] are equal and not equal to prev, they are a common element. Add it to the result and update the prev variable.

If arr1[i] is smaller than the other two elements, increment i.

If arr2[j] is smaller than the other two elements, increment j.

If arr3[k] is smaller than the other two elements, increment k.

Continue this process until any of the pointers reaches the end of its respective array."""
def findCommonElements(arr1, arr2, arr3):
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    i, j, k = 0, 0, 0
    prev = None
    result = []

    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k] and arr1[i] != prev:
            result.append(arr1[i])
            prev = arr1[i]
            i += 1
            j += 1
            k += 1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1

    return result