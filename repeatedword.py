def find_first_repeated_word(s):
    words = s.split()
    seen_words = set()
    
    for word in words:
        if word in seen_words:
            return word
        seen_words.add(word)
    
    return None  # No repeated word found

# Example usage
input_string = "this is a test test"
result = find_first_repeated_word(input_string)
print("First repeated word:", result)  # Output: "test"
