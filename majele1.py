"""majority element problem, which involves finding an element that appears more than n/2 times in an array where n is the size of the array, you can use the Boyer-Moore Voting Algorithm."""
def majorityElement(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    count_candidate = 0

    for num in arr:
        if num == candidate:
            count_candidate += 1

    if count_candidate > len(arr) // 2:
        return candidate
    else:
        return None
