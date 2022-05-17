def rev(a):
    sum=0
    while a>0:
        r=a%10
        sum=sum*10+r
        a=a//10
    return sum
t=int(input())
for i in range(t):
    a=int(input())
    if rev(a)==a:
        print("True")
    else:
        print("False")