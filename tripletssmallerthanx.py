def count_triplets_with_sum_smaller_than(arr, sum):
    arr.sort()
    n = len(arr)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum < sum:
                # If the current triplet satisfies the condition,
                # then all triplets with the current left pointer also satisfy
                count += (right - left)
                left += 1
            else:
                right -= 1

    return count

# Example usage
arr = [5, 1, 3, 4, 7]
sum = 12
result = count_triplets_with_sum_smaller_than(arr, sum)
print("Count of triplets with sum smaller than", sum, ":", result)  # Output: 4
