def word_break(A, B):
    n = len(A)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in B:
            if i >= len(word) and dp[i - len(word)] and A[i - len(word):i] == word:
                dp[i] = True
                break

    return dp[n]

# Example usage
A = "leetcode"
B = ["leet", "code"]
result = word_break(A, B)
if result:
    print("A can be segmented using words from B")
else:
    print("A cannot be segmented using words from B")
