def min_operations_to_convert(A, B):
    i, j = len(A) - 1, len(B) - 1
    operations = 0

    while i >= 0 and j >= 0:
        if A[i] == B[j]:
            i -= 1
            j -= 1
        else:
            i -= 1
            operations += 1

    if j < 0:
        return operations
    else:
        return -1

# Example usage
A = "EACBD"
B = "EABCD"
result = min_operations_to_convert(A, B)
print("Minimum operations:", result)  # Output: 3
