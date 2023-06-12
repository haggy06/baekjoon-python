import sys
num = sys.stdin.readline().rstrip()
for i in range(int(num)):
    print(sum(map(int, sys.stdin.readline().rstrip().split())))
