def min_window_containing_all_chars(s, p):
    char_count = {}
    for char in p:
        char_count[char] = char_count.get(char, 0) + 1

    required_chars = len(char_count)
    formed_chars = 0
    left = right = 0
    min_length = float('inf')
    result_start = 0

    while right < len(s):
        char = s[right]
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                formed_chars += 1

        while formed_chars == required_chars and left <= right:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                result_start = left

            if s[left] in char_count:
                char_count[s[left]] += 1
                if char_count[s[left]] > 0:
                    formed_chars -= 1

            left += 1

        right += 1

    if min_length == float('inf'):
        return "-1"
    return s[result_start:result_start + min_length]

# Example usage
s = "timetopractice"
p = "toc"
result = min_window_containing_all_chars(s, p)
print("Smallest window:", result)  # Output: "toprac"
