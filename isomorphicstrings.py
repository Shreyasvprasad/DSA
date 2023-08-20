def are_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_mapping = {}
    used_chars = set()
    
    for i in range(len(str1)):
        if str1[i] in char_mapping:
            if char_mapping[str1[i]] != str2[i]:
                return False
        else:
            if str2[i] in used_chars:
                return False
            char_mapping[str1[i]] = str2[i]
            used_chars.add(str2[i])
    
    return True

# Example usage
str1 = "egg"
str2 = "add"
result = are_isomorphic(str1, str2)
print("Are the strings isomorphic?", result)  # Output: True
