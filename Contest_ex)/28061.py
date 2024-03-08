N = int(input())
lst = list(map(int, input().split()))
max = 0
for i in range(N):
    value = lst[i] - N + i
    if max < value:
        max = value
print(max)