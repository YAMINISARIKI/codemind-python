def rev(i):
    rev=0
    temp=i
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp//=10
    return rev
n=int(input())
for i in range(2*n):
    if rev(i)==i:
        if i<n:
            x=i
        if i>n:
            y=i
            break
if abs(x-n)<abs(y-n):
    print(x)
if abs(x-n)==abs(y-n):
    print(x,y)
if abs(x-n)>abs(y-n):
    print(y)