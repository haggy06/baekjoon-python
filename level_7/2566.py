maxInt, maxX, maxY = 0, 1, 1
for i in range(9):
    lst = list(map(int, input().split()))
    currentMaxInt = max(lst)
    if maxInt < currentMaxInt:
        maxInt = currentMaxInt
        maxY = i+1
        maxX = lst.index(currentMaxInt)+1
print(maxInt)
print(f"{maxY} {maxX}")