def group_anagrams(strings):
    anagram_groups = {}
    
    for s in strings:
        # Sort the characters of the string
        sorted_s = ''.join(sorted(s))
        
        # Add the string to the corresponding anagram group
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        else:
            anagram_groups[sorted_s] = [s]
    
    result = []
    for group in anagram_groups.values():
        result.append(group)
    
    return result

# Example usage
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strings)
print("Anagram groups:", result)  
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
