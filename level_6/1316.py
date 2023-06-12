n, count = int(input()), 0
for i in range(n):
    word = input()
    lst = set()
    Zword = word[0]
    tf = 1
    for Nword in word:
        if Nword != Zword:
            if Nword in lst:
                tf = 0
                break
            lst.add(Zword)
            Zword = Nword
    count += tf
print(count)