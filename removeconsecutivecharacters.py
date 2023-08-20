def erase_consecutive_duplicates(s):
    result = [s[0]]  # Initialize the result with the first character

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            result.append(s[i])

    return ''.join(result)

# Example usage
input_string = "mississippi"
result = erase_consecutive_duplicates(input_string)
print("String after erasing consecutive duplicates:", result)  # Output: "misisipi"
