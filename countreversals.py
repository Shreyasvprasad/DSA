def min_reversals_to_balance(S):
    if len(S) % 2 != 0:
        return -1  # If the length is odd, it's impossible to balance

    openCount = 0
    closeCount = 0

    for char in S:
        if char == '{':
            openCount += 1
        elif char == '}':
            if openCount > 0:
                openCount -= 1
            else:
                closeCount += 1

    totalReversals = (openCount + 1) // 2 + (closeCount + 1) // 2
    return totalReversals

# Example usage
S = "}{{}}{{{"
result = min_reversals_to_balance(S)
print("Minimum number of reversals required:", result)  # Output: 3
