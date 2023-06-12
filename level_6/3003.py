n = list(map(int, input().split()))
lst = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(lst[i] - n[i], end = " ")