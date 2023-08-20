"""The next permutation of an array of integers is the next lexicographically greater permutation of its integer.def nextPermutation(nums):"""
def nextPermutation(nums):
    # Find the first pair of adjacent elements from the right where nums[i] < nums[i+1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        # Find the smallest element greater than nums[i] to the right of nums[i]
        j = len(nums) - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray from nums[i+1] to the end
    left, right = i+1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    