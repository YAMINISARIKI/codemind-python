n=int(input())
a=list(map(int,input().split()))
c=max(a)
c=str(c)
d=len(c)
x=0
for i in a:
    if len(str(i))==d:
        x+=1
print(x)