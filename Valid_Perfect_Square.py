t=int(input())
for i in range(t):
    x=int(input())
    count=0
    for j in range(1,x):
        if j**2==x:
            count=1
            break
    if count==1:
        print("True")
    else:
        print("False")