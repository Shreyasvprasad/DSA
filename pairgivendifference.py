def has_pair_with_difference(arr, N):
    num_set = set()
    
    for num in arr:
        if (num - N) in num_set or (num + N) in num_set:
            return True
        num_set.add(num)
    
    return False

# Example usage
arr = [5, 20, 3, 2, 50, 80]
N = 78
result = has_pair_with_difference(arr, N)
if result:
    print("There exists a pair with difference", N)
else:
    print("No pair with difference", N, "found")
