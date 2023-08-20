"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space
To find the repeated number in an array nums without modifying the array and using only constant extra space, you can use the "tortoise and hare" algorithm, also known as Floyd's cycle-finding algorithm.

Here's how you can implement this algorithm:

Initialize two pointers, slow and fast, to the first element of the array.

Move slow one step forward and fast two steps forward in each iteration.

Repeat step 2 until slow and fast meet.

Once slow and fast meet, reset slow to the first element of the array and keep fast at its current position.

Move both slow and fast one step forward in each iteration until they meet again.

The meeting point of slow and fast will be the repeated number in the array."""
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Move slow and fast pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset slow to the first element
    slow = nums[0]

    # Move slow and fast pointers until they meet again
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
