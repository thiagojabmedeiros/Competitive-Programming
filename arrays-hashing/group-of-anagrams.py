def groupAnagrams(strs):
    seen = {}
    for s in strs:
        sx = "".join(sorted(s))
        if sx in seen:
            seen[sx] += [s]
        else:
            seen[sx] = [s]

    result = []
    
    for k, v in seen.items():
        result.append(v)

    return result

    
groupAnagrams(["eat","tea","tan","ate","nat","bat"])