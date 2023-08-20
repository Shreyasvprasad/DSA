def count_trailing_zeroes(num):
    count = 0
    divisor = 5
    while num >= divisor:
        count += num // divisor
        divisor *= 5
    return count

def smallest_number_with_n_trailing_zeroes(n):
    low = 0
    high = 5 * n
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if count_trailing_zeroes(mid) >= n:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return result

# Example usage
n = int(input("Enter the value of n: "))
result = smallest_number_with_n_trailing_zeroes(n)
print("Smallest number:", result)
