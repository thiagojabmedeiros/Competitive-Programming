def reverse(s):
    l, r = 0, len(s) - 1
    while l < r:
        x = s[l]
        s[l] = s[r]
        s[r] = x
        l += 1
        r -= 1
    print(s)
reverse(["n","e","e","t"])