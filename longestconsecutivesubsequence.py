"""Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 Initialize a variable max_length to 0 to keep track of the maximum length of the subsequence.

Create a hash set num_set and add all the elements from the array to the set.

Iterate through the array and for each element num:

Check if num-1 exists in num_set. If it does, it means that num is not the starting element of a subsequence and we can skip it.

Otherwise, num is the starting element of a subsequence. Initialize a variable curr_length to 1 and increment num by 1.

While num exists in num_set, increment curr_length by 1 and increment num by 1.
Update max_length as the maximum of max_length and curr_length.

After iterating through the array, max_length will contain the length of the longest subsequence of consecutive integers."""

def longestConsecutiveSubsequence(arr):
    max_length = 0
    num_set = set(arr)

    for num in arr:
        if num - 1 not in num_set:
            curr_length = 1
            curr_num = num + 1

            while curr_num in num_set:
                curr_length += 1
                curr_num += 1

            max_length = max(max_length, curr_length)

    return max_length
