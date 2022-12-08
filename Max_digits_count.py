n=int(input())
a=list(map(int,input().split()))
c=0
max=0
for i in a:
    i=str(i)
    l=len(i)
    if(l>=max):
        max=l
for i in a:
    if len(str(i))==max:
        c+=1
print(c)