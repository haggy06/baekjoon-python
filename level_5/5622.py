n = input()
lst = ['ABC', 'DEF', 'GHI', 'JKL','MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0
for alphabet in n:
    for i in range(len(lst)):
        if alphabet in lst[i]:
            t += i + 3
print(t)