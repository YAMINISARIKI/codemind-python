def rev(n):
    sum=0
    while n>0:
        rem=n%10
        sum=sum*10+rem
        n=n//10
    return sum
n=int(input())
sqrev=rev(n)
if n**2==rev(sqrev**2):
    print("True")
else:
    print("False")