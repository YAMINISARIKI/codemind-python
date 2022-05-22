import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
a=s*(s-a)*(s-b)*(s-c)
area=math.pow(a,0.5)
print("%.2f"%area)