def isPalindrome(S):
    left = 0
    right = len(S) - 1

    while left < right:
        if S[left] != S[right]:
            return False

        left += 1
        right -= 1

    return True
