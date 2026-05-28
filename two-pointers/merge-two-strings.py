def mergeStrings(word1, word2):
    if len(word1) == len(word2):
        greater = word1
        lower = word2
    elif len(word1) > len(word2):
        greater = word1
        lower = word2
    else:
        greater = word2
        lower = word1

    ms = ""
    for g, l in zip(word1, word2):
        ms += g
        ms += l

    if len(greater) != len(lower):
        for c in range(len(lower), len(greater)):
            ms += greater[c]
    return ms

mergeStrings("abc", "xyzddf")