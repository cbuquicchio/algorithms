def string_match(pattern, text, q, base=256):
    m = len(pattern)
    n = len(text)
    h = pow(base, m - 1, q)
    p = 0
    t = 0
    indices_matched = []

    for i in range(m):
        p = (base * p + ord(pattern[i])) % q
        t = (base * t + ord(text[i])) % q

    for s in range(n):
        if p == t and pattern == text[s:s+m]:
            indices_matched.append(s)

        if s < n - m:
            t = (base * (t - ord(text[s]) * h) + ord(text[s+m])) % q
        else:
            break

    return indices_matched
