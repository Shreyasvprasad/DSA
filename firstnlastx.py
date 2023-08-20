def find_first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

def find_last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

def find_first_last_occurrences(arr, x):
    first_occurrence = find_first_occurrence(arr, x)
    last_occurrence = find_last_occurrence(arr, x)
    return first_occurrence, last_occurrence

# Example usage
arr = [2, 4, 10, 10, 10, 18, 20]
x = 10
first_occurrence, last_occurrence = find_first_last_occurrences(arr, x)
print("First Occurrence:", first_occurrence)  # Output: 2
print("Last Occurrence:", last_occurrence)    # Output: 4