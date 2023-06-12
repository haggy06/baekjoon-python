lst = []
for i in range(5):
    inp = list(input())
    lst.append(inp)
for i in range(15):
    for j in range(5):
        try:
            print(lst[j][i], end = "")
        except:
            print("", end = "")
