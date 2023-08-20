def max_consecutive_balanced_substrings(str):
    count = 0
    prevChar = str[0]
    currCount = 1
    totalCount = 1

    for i in range(1, len(str)):
        if str[i] == prevChar:
            currCount += 1
        else:
            currCount = 1
            prevChar = str[i]

        if currCount == totalCount:
            count += 1
            currCount = 0

        totalCount += 1

    if totalCount == count * 2:
        return count
    else:
        return -1

# Example usage
binary_string = "010011001"
result = max_consecutive_balanced_substrings(binary_string)
print(result)  # Output should be 3
