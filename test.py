s1 = "abcdefg"

for i in range(len(s1)):
    if s1[i] == "c":
        x = i

xv = x

while x != xv - 1:
    if x >= len(s1):
        x = 0
    print(s1[x])
    x += 1