def longest_prefix_suffix(s):
    n = len(s)
    length = 0
    i = 0
    j = 1

    while j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
            length = i
        else:
            if i == 0:
                j += 1
            else:
                i = 0

    return length

# Example usage
input_string = "abab"
result = longest_prefix_suffix(input_string)
print("Length of longest proper prefix which is also a proper suffix:", result)  # Output: 1
