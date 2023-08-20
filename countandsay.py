def countAndSay(n):
    if n == 1:
        return "1"

    prev = countAndSay(n-1)
    result = ""
    i = 0

    while i < len(prev):
        count = 1
        j = i + 1

        while j < len(prev) and prev[j] == prev[i]:
            count += 1
            j += 1

        result += str(count) + prev[i]
        i += count

    return result
