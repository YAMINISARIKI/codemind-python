def hn(a):
    sum=0
    while a>0:
        rem=a%10
        sum=sum+rem
        a=a//10
    return sum
a=int(input())
sum=hn(a)
if a%sum==0:
    print("True")
else:
    print("False")