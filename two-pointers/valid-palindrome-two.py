# def validPalindrome(s: str):
#     seen = {}
#     x = 0
#     ss = ""
#     ss2 = ""
#     for c in s:
#         seen[c] = seen.get(c, 0) + 1

#     for i in range(len(s)):
#         if seen[s[i]] == 1 and x == 0:
#             x += 1
#             continue
#         ss += s[i]
#     print(ss)

#     x = 0
#     s = s[::-1]
#     print(s)
#     for i in range(len(s)):
#         if seen[s[i]] == 1 and x == 0:
#             x += 1
#             continue
#         ss2 += s[i]

#     l, r = 0, len(ss) - 1
#     iss = True
#     while l < r:
#         if ss[l] == ss[r]:
#             l += 1
#             r -= 1
#             continue
#         iss = False
#         break

#     l, r = 0, len(ss2) - 1
#     iss2 = True
#     while l < r:
#         if ss2[l] == ss2[r]:
#             l += 1
#             r -= 1
#             continue
#         iss2 = False
#         break
#     print(ss)
#     print(ss2)
#     return iss2 or iss
# s = "abbadc"
# print(validPalindrome(s))