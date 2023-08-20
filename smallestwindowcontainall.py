def smallest_window_with_all_characters(s):
    n = len(s)
    
    # Count the number of unique characters in the string
    unique_chars = len(set(s))
    
    # Initialize variables
    char_count = {}
    start = 0
    min_window_length = float('inf')
    window_length = 0
    
    for end in range(n):
        # Add the current character to the count
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        
        # If all unique characters are present in the current window
        while len(char_count) == unique_chars:
            # Update the minimum window length
            window_length = end - start + 1
            min_window_length = min(min_window_length, window_length)
            
            # Remove the character at the start of the window
            if char_count[s[start]] > 1:
                char_count[s[start]] -= 1
            else:
                del char_count[s[start]]
            start += 1
    
    return min_window_length

# Example usage
s = "aabcbcdbca"
result = smallest_window_with_all_characters(s)
print("Smallest window length:", result)  # Output: 4
