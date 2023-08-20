def printDuplicateCharacters(S):
    char_count = {}

    for ch in S:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    for ch, count in char_count.items():
        if count > 1:
            print(ch, count)
