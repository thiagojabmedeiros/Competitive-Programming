def lengthOfLongestSubstring(string):
    l, r = 0, 0
    maxS = 0
    chars = {}
    while r < len(string):

        if string[r] not in chars:
            chars[string[r]] = 1
        else:
            chars[string[r]] += 1

        while chars[string[r]] > 1:
            chars[string[l]] -= 1
            l += 1 

        maxS = max(maxS, len(string[l:r+1]))
        r += 1
    print(maxS)

string = "pwwkew"
lengthOfLongestSubstring(string)