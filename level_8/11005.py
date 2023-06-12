n, base = map(int, input().split())
ans = []

while True:
    mod = n // base
    digit = n % base
    if digit > 9:
        digit = chr(digit + 55)
    ans.append(digit)

    n = mod
    if mod == 0:
        break

for c in ans[::-1]:
    print(c, end="")
