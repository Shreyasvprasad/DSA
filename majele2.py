"""To find all elements in an integer array that appear more than n/3 times, where n is the size of the array, you can use the Boyer-Moore Voting Algorithm with a modification."""
"""Initialize three variables, candidate1, candidate2, and their respective counts, count1 and count2, to hold the potential majority elements and their counts.

Iterate through the array and for each element num:

If num is equal to candidate1, increment count1 by 1.

If num is equal to candidate2, increment count2 by 1.

If count1 is 0, set num as the new candidate1 and increment count1 to 1.

If count2 is 0, set num as the new candidate2 and increment count2 to 1.

If num is different from both candidate1 and candidate2, decrement count1 and count2 by 1.

After iterating through the array, we have two potential candidates for majority elements.

To verify if the candidates appear more than n/3 times, iterate through the array again and count their occurrences.

If the count of candidate1 is greater than n/3, add it to the result list.

If the count of candidate2 is greater than n/3 and it is different from candidate1, add it to the result list.

Return the result list containing the elements that appear more than n/3 times."""
def majorityElements(arr):
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0

    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    count_candidate1 = 0
    count_candidate2 = 0
    result = []

    for num in arr:
        if num == candidate1:
            count_candidate1 += 1
        elif num == candidate2:
            count_candidate2 += 1

    if count_candidate1 > len(arr) // 3:
        result.append(candidate1)

    if count_candidate2 > len(arr) // 3 and candidate2 != candidate1:
        result.append(candidate2)

    return result
