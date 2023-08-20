"""There are 2 sorted arrays A and B of size n each. Write an program to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n)"""
"""Initialize two pointers, i and j, to keep track of the current elements in A and B, respectively. Set them to 0.

Initialize an empty list, merged, to store the merged array.

While i < n and j < n, perform the following steps:

If A[i] is less than or equal to B[j], append A[i] to merged and increment i by 1.

Otherwise, append B[j] to merged and increment j by 1.

If i is less than n, append the remaining elements of A to merged.

If j is less than n, append the remaining elements of B to merged.

If the length of merged is even, the median is the average of the middle two elements. Return the average of merged[n-1] and merged[n].

If the length of merged is odd, the median is the middle element. Return merged[n]."""
def findMedianSortedArrays(A, B):
    n = len(A)
    i = 0
    j = 0
    merged = []

    while i < n and j < n:
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1

    while i < n:
        merged.append(A[i])
        i += 1

    while j < n:
        merged.append(B[j])
        j += 1

    if len(merged) % 2 == 0:
        middle = len(merged) // 2
        return (merged[middle - 1] + merged[middle]) / 2
    else:
        middle = len(merged) // 2
        return merged[middle]
