min = int(input())
max = int(input())
lst = []
for num in range(min, max+1):
    prime = True
    for i in range(2, num-1):
        if num % i == 0:
            prime = False
            break
    if prime and num != 1:
        lst.append(num)
if len(lst) != 0:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)