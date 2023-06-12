n, count = input(), 0
for i in range(len(n)):
    if i >= 1:
        if n[i] == "=":
            if n[i - 1] in ["c", "s"]:
                count -= 1
            if n[i - 1] == "z":
                count -= 1
                if i >= 2:
                    if n[i - 2] == "d":
                        count -= 1
        if n[i] == "-":
            if n[i - 1] in ["c", "d"]:
                count -= 1
        if n[i] == "j":
            if n[i - 1] in ["l", "n"]:
                count -= 1
    count += 1
print(count)