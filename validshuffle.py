def isValidShuffle(s, s1, s2):
    if len(s) != len(s1) + len(s2):
        return False

    i = 0
    j = 0

    for k in range(len(s)):
        if i < len(s1) and s[k] == s1[i]:
            i += 1
        elif j < len(s2) and s[k] == s2[j]:
            j += 1
        else:
            return False

    return True
