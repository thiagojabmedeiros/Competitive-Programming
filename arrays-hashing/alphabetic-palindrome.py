def isPalindromeAlphabetic(code: str):
    l, r = 0, len(code) -  1
    while l < r:
        if not code[l].isalpha():
            l += 1
            continue
        if not code[r].isalpha():
            r -= 1
            continue
        if code[l].lower() != code[r].lower():
            return 0
        l += 1
        r -= 1
    return 1

string = "th1,ia?g.o!2"
isPalindromeAlphabetic(string)