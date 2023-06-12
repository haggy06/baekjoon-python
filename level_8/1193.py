num = int(input())
scope, i = 0, 1
while True:
    scope += i
    if num <= scope:
        line = i
        num -= scope - i + 1
        break
    i += 1
mo, ja = 1, line
for j in range(line):
    if j == num:
        if line%2 == 0:
            print(f"{mo}/{ja}")
        else:
            print(f"{ja}/{mo}")
    mo += 1
    ja -= 1