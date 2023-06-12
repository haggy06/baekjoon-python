n = int(input())
for i in range(n):
    a, lst = input().split()
    for h in lst:
        for j in range(int(a)):
            print(h, end="")
    print()