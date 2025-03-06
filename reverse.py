def reverse(s, k):
    s = list(s)
    if len(s) > 2 * k:
        for i in range(0, len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]

        return ''.join(s)
    
    elif len(s) >= k:
        s[:k] = s[:k][::-1]

        return ''.join(s)

