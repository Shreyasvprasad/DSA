"""Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""
"""Initialize two pointers, left = 0 and right = 0, to represent the current subarray.

Initialize a variable min_length = infinity to keep track of the minimal length of the subarray.

Initialize a variable curr_sum = 0 to keep track of the current sum of the subarray.

While right < length of nums, perform the following steps:

Add nums[right] to curr_sum.

While curr_sum is greater than or equal to the target, update min_length to the minimum of min_length and right - left + 1, and subtract nums[left] from curr_sum. Then, increment left by 1 to move the left pointer.

Increment right by 1 to move the right pointer.

After the iterations, if min_length is still infinity, return 0 to indicate that there is no subarray with a sum greater than or equal to the target.Otherwise, return min_length"""
def minSubarrayLength(nums, target):
    left = 0
    right = 0
    min_length = float('inf')
    curr_sum = 0

    while right < len(nums):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

        right += 1

    if min_length == float('inf'):
        return 0
    else:
        return min_length
