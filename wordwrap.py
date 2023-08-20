def min_badness_line_break(nums, line_width):
    n = len(nums)
    dp = [float('inf')] * n
    breaks = [0] * n
    dp[0] = (line_width - nums[0])**3

    for i in range(1, n):
        total_length = nums[i]
        dp[i] = dp[i - 1] + (line_width - nums[i])**3
        breaks[i] = i

        for j in range(i - 1, -1, -1):
            total_length += nums[j] + 1  # Adding 1 for the space after the word
            if total_length > line_width:
                break

            cost = 0 if j == 0 else dp[j - 1]
            cost += (line_width - total_length)**3

            if cost < dp[i]:
                dp[i] = cost
                breaks[i] = j

    lines = []
    i = n - 1
    while i >= 0:
        lines.append((breaks[i], i))
        i = breaks[i] - 1

    lines.reverse()
    return lines

# Example usage
nums = [3, 2, 2, 5]
line_width = 6
line_breaks = min_badness_line_break(nums, line_width)
for start, end in line_breaks:
    print(nums[start:end+1])  # Print words in each line
