"""Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K."""
"""Initialize a hashmap to store the frequency of each element in the array.

Iterate through the array and for each element num, calculate the target value target = K - num.

Check if target exists in the hashmap. If it does, increment the count of pairs by the frequency of target in the hashmap.

Increment the frequency of num in the hashmap.

After iterating through the array, the count of pairs will contain the number of pairs whose sum is equal to K."""
def countPairs(arr, K):
    count = 0
    frequency = {}

    for num in arr:
        target = K - num
        if target in frequency:
            count += frequency[target]
        frequency[num] = frequency.get(num, 0) + 1

    return count
