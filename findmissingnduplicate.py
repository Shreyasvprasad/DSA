def find_missing_and_duplicate_numbers(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    total_square_sum = n * (n + 1) * (2 * n + 1) // 6

    arr_sum = sum(arr)
    arr_square_sum = sum(num ** 2 for num in arr)

    difference_sum = total_sum - arr_sum
    difference_square_sum = total_square_sum - arr_square_sum

    duplicate_number = (difference_sum + difference_square_sum // difference_sum) // 2
    missing_number = duplicate_number - difference_sum

    return missing_number, duplicate_number

# Example usage
arr = [4, 3, 2, 7, 8, 2, 1]
missing_number, duplicate_number = find_missing_and_duplicate_numbers(arr)
print("Missing Number:", missing_number)
print("Duplicate Number:", duplicate_number)
