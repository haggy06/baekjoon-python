n = input()
lst = [-1 for i in range(26)]
for i in range(len(n)):
    c = ord(n[i]) - 97
    if lst[c] == -1:
        lst[c] = i
print(*lst)