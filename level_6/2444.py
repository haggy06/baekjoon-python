n = int(input())
for i in range(n):
    print(" "*(n-i-1),end="*")
    print("*"*(2*i))
for i in range(n):
    if i != 0:
        print(" "*(i),end="*")
        print("*"*2*(n-i-1))