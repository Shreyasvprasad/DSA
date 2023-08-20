"""Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
To merge two sorted arrays arr1 and arr2 in sorted order without using any extra space, you can use the following approach:

Initialize three variables: i to keep track of the current index in arr1, j to keep track of the current index in arr2, and k to keep track of the current index in the merged array.

Start with i pointing to the last element of arr1 and j pointing to the last element of arr2.

Compare the elements at arr1[i] and arr2[j]. If arr1[i] is greater than arr2[j], it means the element from arr1 should come later in the merged array.

Move the element from arr1[i] to arr2[j] and decrement i by 1.

If arr1[i] is smaller than or equal to arr2[j], it means the element from arr2 should come later in the merged array.

Decrement j by 1 and repeat steps 3 to 6 until j becomes -1 or all elements in arr1 have been processed.

After the above steps, arr2 will have the merged array in reverse order. To obtain the merged array in sorted order, you can reverse arr2 using an appropriate method or loop."""
def mergeArrays(arr1, arr2, n, m):
    i = n - 1
    j = m - 1
    k = n + m - 1

    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr2[k] = arr1[i]
            i -= 1
        else:
            arr2[k] = arr2[j]
            j -= 1
        k -= 1

    while j >= 0:
        arr2[k] = arr2[j]
        j -= 1
        k -= 1

    # Reverse arr2 to get the merged array in sorted order
    arr2.reverse()
