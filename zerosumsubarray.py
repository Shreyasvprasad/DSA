"""Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.
Initialize a variable curr_sum to 0.

Initialize an empty hashmap sum_map.

Iterate through the array and for each element num:

Add num to curr_sum.

If curr_sum is 0 or if curr_sum is already present in sum_map, it means that a subarray with a sum of 0 exists. Return True.

Add curr_sum to sum_map along with its index as the value.

If no subarray with a sum of 0 is found after iterating through the array, return False."""
def hasZeroSumSubarray(arr):
    curr_sum = 0
    sum_map = {}

    for i, num in enumerate(arr):
        curr_sum += num

        if curr_sum == 0 or curr_sum in sum_map:
            return True

        sum_map[curr_sum] = i

    return False
