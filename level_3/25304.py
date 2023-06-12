a = int(input())
b = int(input())
c = 0
for i in range(b):
    p, n = map(int, input().split())
    c += p * n
if a == c:
    print("Yes")
else:
    print("No")