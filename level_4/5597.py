lst = [0 for i in range(30)]
n = 1
for i in range(28):
    lst[int(input()) - 1] = 1
for i in lst:
    if i == 0:
        print(n)
    n += 1