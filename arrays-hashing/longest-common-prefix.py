def longestCommonPrefix(strs):
    seen = {}
    for word in strs:
        prefix = ""
        for c in word:
            prefix += c
            seen[prefix] = seen.get(prefix, 0) + 1

    sortArr = []

    for k, v in seen.items():
        if v < len(strs): 
            continue
        sortArr.append([v, k])

    sortArr = sorted(sortArr)
    # print(sortArr)

    if len(sortArr) > 0:
        print(sortArr[-1][1])
    else:
        return ""


longestCommonPrefix(["a"])