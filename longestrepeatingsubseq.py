def longestRepeatingSubsequence(str):
    n = len(str)
    
    # Create a DP table to store the lengths of longest repeating subsequences
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if str[i - 1] == str[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the longest repeating subsequence is stored in dp[n][n]
    return dp[n][n]

# Example usage
str = "aabcaab"
print(longestRepeatingSubsequence(str))  # Output: 3
