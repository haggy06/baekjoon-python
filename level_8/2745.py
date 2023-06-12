inp, n = input().split()
inp = inp[::-1]
ans = 0
for i in range(len(inp)):
    char = ord(inp[i])
    if char > 60:
        ans += int(n)**(i)*(char - 55)
    else:
        ans += int(n)**(i)*(char - 48)
print(ans)


