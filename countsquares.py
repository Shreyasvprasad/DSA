def count_perfect_squares_less_than_N(N):
    # Find the largest perfect square less than N
    largest_square_root = int(N ** 0.5)
    largest_perfect_square = largest_square_root ** 2

    # Count the number of perfect squares up to the largest square
    count = largest_square_root

    return count

# Example usage
N = 20
result = count_perfect_squares_less_than_N(N)
print("Number of perfect squares less than", N, ":", result)
