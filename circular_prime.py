n=int(input())
count=0
c=0
for j in range(1,n+1):
    if n%j==0:
        count+=1
if count==2:
    n=str(n)
    n=n[::-1]
    n=int(n)
    for j in range(1,n+1):
        if n%j==0:
            c+=1
    if c==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")