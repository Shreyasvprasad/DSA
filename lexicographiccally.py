def next_permutation(arr):
    n = len(arr)
    i = n - 2

    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1

    if i == -1:
        arr.reverse()
        return

    j = n - 1
    while j > i and arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = arr[i+1:][::-1]

# Example usage
arr = [1, 2, 3]
next_permutation(arr)
print(arr)  # Output: [1, 3, 2]

arr = [3, 2, 1]
next_permutation(arr)
print(arr)  # Output: [1, 2, 3]

arr = [1, 1, 5]
next_permutation(arr)
print(arr)  # Output: [1, 5, 1]
