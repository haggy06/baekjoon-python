while True:
    lst = []
    a = int(input())
    if  a == -1:
        break
    else:
        for i in range(1, a):
            if a - a // i * i == 0:
                lst.append(i)
        if a == sum(lst):
            lst = list(map(str, lst))
            print(f"{a} = {' + '.join(lst)}")
        else:
            print(f"{a} is NOT perfect.")