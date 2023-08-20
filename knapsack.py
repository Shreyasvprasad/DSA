def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

n = int(input("Enter the number of items: "))
values = [int(x) for x in input("Enter the values of items: ").split()]
weights = [int(x) for x in input("Enter the weights of items: ").split()]
capacity = int(input("Enter the knapsack capacity: "))
max_value = knapsack_01(values, weights, capacity)
print("Maximum value:", max_value)
