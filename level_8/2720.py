n = int(input())
for i in range(n):
    inp = int(input())
    print(f"{inp//25} {(inp%25)//10} {((inp%25)%10)//5} {((inp%25)%10)%5}")