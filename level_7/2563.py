lst = [[0 for i in range(100)] for i in range(100)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for y1 in range(10):
        for x1 in range(10):
            lst[y+y1][x+x1] = 1
print(sum(map(sum, lst)))