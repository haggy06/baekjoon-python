h,m=map(int,input().split())
r=int(input())+m
print((h+r//60)%24,r%60)
