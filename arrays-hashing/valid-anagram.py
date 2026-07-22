def isAnagram(s1, s2):
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))

    return s2 == s1

s1 = "thiago"
s2 = "oghait"

print(isAnagram(s1, s2))