p, m, h = map(int, input().split())
print(int((h-p)/(p-m))+1+int((h-p)%(p-m)!=0))