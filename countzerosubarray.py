def count_subarrays_with_sum_zero(arr):
    n = len(arr)
    prefix_sum = 0
    prefix_sum_count = {}  # Hash map to store prefix sum frequencies
    count = 0  # Count of sub-arrays with sum 0
    
    for i in range(n):
        prefix_sum += arr[i]
        
        if prefix_sum == 0:
            count += 1
        
        if prefix_sum in prefix_sum_count:
            count += prefix_sum_count[prefix_sum]
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1
    
    return count

# Example usage
arr = [4, 2, -3, -1, 0, 4]
result = count_subarrays_with_sum_zero(arr)
print("Total count of sub-arrays with sum 0:", result)  # Output: 2
