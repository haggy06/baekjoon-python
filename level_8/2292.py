num = int(input())
scope, i = 2, 0
while True:
    scope += 6*i
    if num < scope:
        print(i+1)
        break;
    i += 1