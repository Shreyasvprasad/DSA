def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the array
    min_length = min(len(s) for s in strs)
    
    # Iterate through characters in the shortest string
    for i in range(min_length):
        current_char = strs[0][i]
        for s in strs[1:]:
            if s[i] != current_char:
                return s[:i]
    
    return strs[0][:min_length]

# Example usage
string_array = ["flower", "flow", "flight"]
result = longest_common_prefix(string_array)
print("Longest common prefix:", result)  # Output: "fl"
