import math
n = int(input())
for i in range(n):
    count = 0
    lst = list(map(int, input().split()))
    average = sum(lst[1:]) / lst[0]
    for j in lst[1:]:
        if j > average:
            count += 1
    print(f"{count / lst[0] * 100:.3f}%")