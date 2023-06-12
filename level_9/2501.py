a, b = map(int, input().split())
lst = []
for i in range(a):
    if a - a // (i+1) * (i+1) == 0:
        lst.append(i+1)

try:
    print(lst[b-1])
except:
    print(0)