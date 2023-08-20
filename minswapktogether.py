"""Given an array arr of n positive integers and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray."""
"""Count the number of elements in arr that are less than or equal to k. Let's call this count count_k.

Initialize two pointers, left = 0 and right = 0, to represent the current window.

Initialize a variable max_count = 0 to keep track of the maximum count of elements less than or equal to k in any window.

While right < n, perform the following steps:

Increment count_k if arr[right] is less than or equal to k.

Increment right by 1 to expand the window.

While the size of the window (right - left) is greater than count_k, perform the following steps:

Decrement count_k if arr[left] is less than or equal to k.

Increment left by 1 to shrink the window.

Update max_count to the maximum of max_count and count_k.

The minimum number of swaps required is given by count_k - max_count."""
def minSwaps(arr, k):
    n = len(arr)
    count_k = 0
    max_count = 0

    for i in range(n):
        if arr[i] <= k:
            count_k += 1

    left = 0
    right = 0

    while right < n:
        if arr[right] <= k:
            count_k += 1

        right += 1

        while (right - left) > count_k:
            if arr[left] <= k:
                count_k -= 1

            left += 1

        max_count = max(max_count, count_k)

    return count_k - max_count
