def charactherReplacement(s, k):
    l, r = 0, 0
    maxS = 0
    kx = 0
    sx = ""
    seen = {}

    for c in s:
        seen[c] = seen.get(c, 0) + 1
    greater = []
    for key, value in seen.items():
        greater.append([value, key])
    greater = sorted(greater)
    greater = greater[-1][1]

    while r < len(s):
        if s[r] != greater and kx < k:
            kx += 1
            sx += greater
        else:
            sx += s[r]
        maxS = max(maxS, len(sx))
        r += 1
    print(maxS)
    
charactherReplacement('AAABABB', 1)