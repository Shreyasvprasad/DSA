MOD = 10**9 + 7

def count_palindromic_subsequences(str):
    N = len(str)
    dp = [[0] * N for _ in range(N)]
    
    for i in range(N):
        dp[i][i] = 1
    
    for cl in range(2, N + 1):
        for i in range(N - cl + 1):
            j = i + cl - 1
            if str[i] != str[j]:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % MOD
    
    return dp[0][N - 1]

# Example usage
str = "abcb"
result = count_palindromic_subsequences(str)
print("Number of palindromic subsequences:", result)  # Output: 6
