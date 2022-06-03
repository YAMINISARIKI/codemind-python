n=int(input())
a=list(map(int,input().split()))
e=o=0
for i in range(n):
    if i%2==0:
        e+=a[i]
    else:
        o+=a[i]
diff=abs(e-o)
if diff%4==0:
    print("X")
else:
    print("Y")