n=int(input())
a=list(map(int,input().split()))
c=0
x=[]
maxi=0
for i in a:
    if i==1:
        c+=1
        maxi=max(c,maxi)
    else:
        c=0
print(maxi)