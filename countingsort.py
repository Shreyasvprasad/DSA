def counting_sort(arr):
    max_val = max(arr) + 1
    count = [0] * max_val
    output = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

# Example usage
arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Sorted array (Counting Sort):", arr)
