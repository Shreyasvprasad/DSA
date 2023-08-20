def largest_common_subsquare(A, B):
    n, m = len(A), len(A[0])
    x, y = len(B), len(B[0])
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, x + 1):
                for l in range(1, y + 1):
                    if A[i - 1][j - 1] == B[k - 1][l - 1]:
                        dp[k][l] = dp[k - 1][l - 1] + 1
                        max_len = max(max_len, dp[k][l])

    return max_len

# Example usage
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[4, 5],
     [7, 8]]

result = largest_common_subsquare(A, B)
print("Largest common subsquare length:", result)  # Output: 2
