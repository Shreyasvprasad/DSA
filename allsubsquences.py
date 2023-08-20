def generateSubsequencesUtil(str, current, index):
    # If we have reached the end of the string
    if index == len(str):
        # Print the current subsequence
        print(''.join(current))
        return
    
    # Include the current character
    generateSubsequencesUtil(str, current + [str[index]], index + 1)
    
    # Exclude the current character
    generateSubsequencesUtil(str, current, index + 1)

def generateSubsequences(str):
    generateSubsequencesUtil(str, [], 0)

# Example usage
str = "abc"
generateSubsequences(str)
