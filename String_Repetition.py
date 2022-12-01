a=input()
n=int(input())
c=0
c1=0
for i in a:
    if i=="a":
        c+=1
    x=n//len(a)
    y=n%len(a)
c2=0
c1=0
if i!=y:
    for i in a:
        c1+=1
        if c1<=y:
            if i =="a":
                c2+=1
print((c*x)+c2)
                