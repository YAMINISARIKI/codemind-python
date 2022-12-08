x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=0
for i in b:
    if i in a:
        a.remove(i)
        d+=1
if d==y:
    print("Yes")
else:
    print("No")