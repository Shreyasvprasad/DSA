def longestPalindrome(S):
    n = len(S)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    for i in range(n-1, -1, -1):
        dp[i][i] = True

        for j in range(i+1, n):
            if S[i] == S[j] and (j - i == 1 or dp[i+1][j-1]):
                dp[i][j] = True

                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    start = i

    return S[start:start+max_len]
