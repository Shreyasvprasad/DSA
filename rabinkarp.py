def search_pattern(pat, txt):
    m = len(pat)
    n = len(txt)
    prime = 101  # A prime number for hash calculation

    def calculate_hash(s):
        h = 0
        for i in range(len(s)):
            h = (h * prime + ord(s[i])) % prime
        return h

    pat_hash = calculate_hash(pat)
    txt_hash = calculate_hash(txt[:m])

    for i in range(n - m + 1):
        if pat_hash == txt_hash:
            if txt[i:i + m] == pat:
                print("Pattern found at index:", i)

        if i < n - m:
            txt_hash = (txt_hash - ord(txt[i]) * (prime**(m - 1))) % prime
            txt_hash = (txt_hash * prime + ord(txt[i + m])) % prime
            txt_hash = (txt_hash + prime) % prime

# Example usage
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
search_pattern(pat, txt)
