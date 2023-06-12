n = int(input())
l = map(int, input().split())
v = int(input())
a = 0
for i in l:
    if i == v:
        a += 1
print(a)