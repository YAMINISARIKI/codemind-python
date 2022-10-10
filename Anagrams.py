n=input()
m=input()
n=n.lower()
m=m.lower()
c=0
c1=0
for i in n:
    c1+=1
    if i in m:
        c+=1
if(c==c1):
    print("True")
else:
    print("False")
