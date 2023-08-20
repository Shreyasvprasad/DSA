def count_subsets_with_sum_between(arr, n, A, B):
    dp = [0] * (B - A + 1)
    dp[0] = 1
    
    for num in arr:
        if num >= A and num <= B:
            for i in range(B, num - 1, -1):
                dp[i - num] += dp[i]
    
    total_count = 0
    for i in range(A, B + 1):
        total_count += dp[i - A]
    
    return total_count

# Example usage
N, A, B = map(int, input().split())
S = []
for _ in range(N):
    S.append(int(input()))
result = count_subsets_with_sum_between(S, N, A, B)
print(result)
