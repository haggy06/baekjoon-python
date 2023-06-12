N, M = map(int, input().split())
lst = [[0 for i in range(M)] for i in range(N)]
for x in range(2):
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(len(inp)):
            lst[i][j] += inp[j]
for i in lst:
    print(*i)