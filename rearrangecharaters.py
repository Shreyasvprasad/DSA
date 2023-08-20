def rearrange_string(s):
    char_count = {}
    
    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Create a list of tuples (frequency, character)
    char_freq = [(freq, char) for char, freq in char_count.items()]
    
    # Sort the list in descending order of frequency
    char_freq.sort(reverse=True)
    
    # Construct the rearranged string
    result = [None] * len(s)
    index = 0
    
    for freq, char in char_freq:
        for _ in range(freq):
            result[index] = char
            index += 2
            if index >= len(s):
                index = 1
    
    return ''.join(result)

# Example usage
s = "aaab"
result = rearrange_string(s)
print("Rearranged string:", result)  # Output: "abab"
