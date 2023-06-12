a = int(input())
print('01'[(a%4==0and a%100!=0)or a%400==0])
