"""Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Initialize two pointers, pos and neg, to keep track of the positions where the next positive and negative numbers should be placed.

Iterate through the array and for each element num:

If num is positive and the current position is already occupied by a positive number, find the next available position for a positive number by incrementing pos until an empty spot is found.

If num is negative and the current position is already occupied by a negative number, find the next available position for a negative number by incrementing neg until an empty spot is found.

Place num in the appropriate position based on its sign (positive or negative).

After iterating through the array, the resulting array will contain alternate positive and negative numbers without changing the relative order of positive and negative numbers."""
def alternatePosNeg(arr):
    n = len(arr)
    pos, neg = 0, 0

    while pos < n and neg < n:
        # Find next available position for positive number
        while pos < n and arr[pos] < 0:
            pos += 1

        # Find next available position for negative number
        while neg < n and arr[neg] >= 0:
            neg += 1

        if pos < n and neg < n:
            # Swap positive and negative numbers
            arr[pos], arr[neg] = arr[neg], arr[pos]

    return arr
