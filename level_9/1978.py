def isprime(inp: int) -> bool:
    lst = []
    for i in range(1, inp):
        if inp - inp // i * i == 0:
            lst.append(i)
    if len(lst) < 2:
        return True
    else:
        return False

n = input()
lstInp = list(map(int, input().split()))
num = 0
for a in lstInp:
    if a != 1:
        num += int(isprime(a))
print(num)



