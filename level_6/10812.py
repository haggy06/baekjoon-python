a, n = map(int, input().split())
lst = [i+1 for i in range(a)]
Blst, Elst = [], []
count = 0
for i in range(n):
    count = 0
    Blst, Elst = [], []
    b, e, m = map(int, input().split())
    for j in range(e):
        if j >= m-1:
            Elst.append(lst[j])
    for j in range(m):
        if j >= b - 1:
            Blst.append(lst[j])
    for c in range(e):
        if c >= b-1:
            try:
                lst[c] = Elst[count]
            except:
                lst[c] = Blst[count-len(Elst)]
            count += 1
print(*lst)