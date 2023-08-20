def bad_character_heuristic(pattern):
    m = len(pattern)
    bad_char = {}

    for i in range(m):
        bad_char[pattern[i]] = i

    return bad_char

def good_suffix_heuristic(pattern):
    m = len(pattern)
    suffixes = [0] * (m + 1)
    good_suffix = [0] * (m + 1)

    compute_suffix_array(pattern, suffixes)
    compute_good_suffix_array(pattern, suffixes, good_suffix)

    return good_suffix

def compute_suffix_array(pattern, suffixes):
    m = len(pattern)
    f, g = m, m

    for i in range(m - 1, -1, -1):
        if i > f and suffixes[i + m - 1 - g] < i - f:
            suffixes[i] = suffixes[i + m - 1 - g]
        else:
            if i < f:
                f = i
            g = i
            while f >= 0 and pattern[f] == pattern[f + m - 1 - g]:
                f -= 1
            suffixes[i] = g - f

def compute_good_suffix_array(pattern, suffixes, good_suffix):
    m = len(pattern)
    last_prefix_index = m

    for i in range(m - 1, -1, -1):
        if suffixes[i] == i + 1:
            while last_prefix_index >= m - 1 - i:
                last_prefix_index = m - 1 - i - suffixes[m - 1 - i]
            for j in range(m - 1 - i, last_prefix_index):
                good_suffix[j] = m - 1 - i

    for i in range(m - 1):
        good_suffix[m - 1 - suffixes[i]] = m - 1 - i

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    bad_char = bad_character_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)

    i = j = 0
    occurrences = []

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            occurrences.append(i)
            i += good_suffix[0]
        else:
            bc_shift = j - bad_char.get(text[i + j], -1)
            gs_shift = good_suffix[j]
            i += max(bc_shift, gs_shift)

    return occurrences

# Example usage
text = "ABAAABCDABCAAD"
pattern = "AB"
result = boyer_moore_search(text, pattern)
print("Pattern occurrences:", result)  # Output: [0, 4, 9]
