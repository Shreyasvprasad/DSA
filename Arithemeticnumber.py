def is_b_in_arithmetic_sequence(A, C, B):
    diff = B - A
    if diff % C == 0:
        return 1
    return 0

# Example usage
A = int(input("Enter the first term A: "))
C = int(input("Enter the common difference C: "))
B = int(input("Enter the integer B: "))
result = is_b_in_arithmetic_sequence(A, C, B)
print(result)
