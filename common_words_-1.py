n1=input()
n1=n1.lower()
n1=n1.split()
n1=set(n1)
n2=input()
n2=n2.lower()
n2=n2.split()
n2=set(n2)
c=0
for i in n1:
    if i in n2:
        if i!=" ":
            c+=1
print(c)
            
        