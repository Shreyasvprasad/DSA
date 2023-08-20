"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays."""
"""Calculate the total length of the merged array as total_length = m + n.

Initialize two pointers, i and j, to keep track of the current elements in nums1 and nums2, respectively. Set them to 0.

Initialize two variables, prev and curr, to keep track of the two elements that are candidates for the median. Set them to 0.

Iterate total_length // 2 + 1 times:

Set prev to curr.

If i is less than m and j is less than n:

If nums1[i] is less than or equal to nums2[j], set curr to nums1[i] and increment i by 1.
Otherwise, set curr to nums2[j] and increment j by 1.
Otherwise, if i is less than m, set curr to nums1[i] and increment i by 1.

Otherwise, set curr to nums2[j] and increment j by 1.

If total_length is odd, the median is curr. Otherwise, the median is the average of prev and curr."""
def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    total_length = m + n

    i = 0
    j = 0
    prev = 0
    curr = 0

    for _ in range(total_length // 2 + 1):
        prev = curr

        if i < m and j < n:
            if nums1[i] <= nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        elif i < m:
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if total_length % 2 == 1:
        return curr
    else:
        return (prev + curr) / 2
