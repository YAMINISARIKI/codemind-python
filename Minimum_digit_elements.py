n=int(input())
x=list(map(int,input().split()))
p=min(x)
c=0
for i in x:
    if len(str(p))==len(str(i)):
        c+=1
print(c)