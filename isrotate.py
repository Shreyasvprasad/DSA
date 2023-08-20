def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False

    temp = s1 + s1

    return isSubstring(temp, s2)

def isSubstring(s, pattern):
    n = len(s)
    m = len(pattern)
    lps = computeLPS(pattern)

    i = 0  # index for s
    j = 0  # index for pattern

    while i < n:
        if s[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                return True
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return False

def computeLPS(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix

    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

    return lps
