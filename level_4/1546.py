a = int(input()) * 0
lst = list(map(int, input().split()))
lstest = max(lst)
for i in lst:
    a += i / lstest * 100
print(a / len(lst))