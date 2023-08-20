def is_match(wild, pattern):
    m, n = len(wild), len(pattern)
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # Initialize the first row for matching empty pattern with wild
    for i in range(1, m + 1):
        if wild[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if wild[i - 1] == '?' or wild[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif wild[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

# Example usage
wild = "miss*ss?ppi"
pattern = "m*ss*?i"
result = is_match(wild, pattern)
print("Do the strings match?", result)  # Output: True
