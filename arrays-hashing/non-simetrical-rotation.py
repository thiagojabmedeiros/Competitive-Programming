def nonSimetricalRotate(s1, s2):
    if s1 == s2:
        return 0
    
    if len(s1) != len(s2):
        return 0
    
    if s2 in s1+s1:
        return 1
    
    return 0

    # if s1 == s2:
    #     return 0
    
    # for i in range(len(s2)):
    #     if s2[i] == s1[0]:
    #         x = i

    # xv = x
    # y = 0
    # while x != xv - 1:
    #     if x >= len(s2):
    #         x = 0
    #     if s1[y] == s2[x]:
    #         x += 1
    #         y += 1
    #     else:
    #         return 0
    #     if x == xv - 1 and s1[y] == s2[x]:
    #         continue
    #     else: 
    #         return 0
    # return 1
        
        

print(nonSimetricalRotate("abcd", "bcda"))