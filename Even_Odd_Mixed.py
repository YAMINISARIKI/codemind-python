n=int(input())
oc=0
ec=0
while n:
    rem=n%10
    if rem%2==0:
        ec+=1
    else:
        oc+=1
    n=n//10
if ec!=0 and oc==0:
    print("Even")
elif ec==0 and oc!=0:
    print("Odd")
elif ec!=0 and oc!=0:
    print("Mixed")