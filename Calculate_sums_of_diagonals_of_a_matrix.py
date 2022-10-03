n=int(input())
s1=0
s2=0
for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(0,n):
        s1=s1+a[i-1]
        break
    for j in range(0,n):
        s2=s2+a[n-i]
        break
print("Principal Diagonal:"+str(s1))
print("Secondary Diagonal:"+str(s2))