"""You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.
 
Return the minimum number of moves needed to make s a palindrome."""
"""Initialize two pointers, left = 0 and right = len(s) - 1, to represent the left and right ends of the string.

Initialize a variable moves = 0 to keep track of the minimum number of moves needed.

While left < right, perform the following steps:

If s[left] is equal to s[right], move the pointers inward by incrementing left and decrementing right.

If s[left] is not equal to s[right], increment moves by 1 and move the pointer right inward by decrementing right.

After the iterations, the minimum number of moves needed to make s a palindrome is given by moves."""
def minMovesToMakePalindrome(s):
    left = 0
    right = len(s) - 1
    moves = 0

    while left < right:
        if s[left] != s[right]:
            moves += 1
            right -= 1
        else:
            left += 1
            right -= 1

    return moves
