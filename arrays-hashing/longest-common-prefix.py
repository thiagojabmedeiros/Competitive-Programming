def longestCommonPrefix(strs):
    seen = {}
    arr = []

    for s in strs:
        prefix = ""
        for c in s:
            prefix += c
            if len(prefix) > 1:
                seen[prefix] = seen.get(prefix, 0) + 1

    for k, v in seen.items():
        if v == len(strs):
            arr.append([v, k])

    arr.sort()
    return arr[-1][1]

strs = ["dance","dag","danger","damage"]
longestCommonPrefix(strs)