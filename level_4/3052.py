lst = [0 for i in range(42)]
n = 0
for i in range(10):
    a = int(input())%42
    if lst[a] == 0:
        n += 1
        lst[a] = 1
print(n)