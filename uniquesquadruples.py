def find_quadruples(arr, target_sum):
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = arr[i] + arr[j] + arr[left] + arr[right]

                if current_sum == target_sum:
                    result.append((arr[i], arr[j], arr[left], arr[right]))
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target_sum:
                    left += 1
                else:
                    right -= 1

    return result

# Example usage
arr = [1, 0, -1, 0, -2, 2]
target_sum = 0
result = find_quadruples(arr, target_sum)
print("Unique quadruples that sum up to", target_sum, ":", result)
