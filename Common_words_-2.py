n1=input()
n1=n1.lower()
n1=n1.split()
n1=list(n1)
n2=input()
n2=n2.lower()
n2=n2.split()
n2=list(n2)
c=0
for i in n1:
    if n1.count(i)>1:
        if i in n2:
            n2.remove(i)
for j in n2:
    if n2.count(j)>1:
        if j in n1:
            n1.remove(j)
for i in n1:
    if i in n2:
        if i!=" ":
            c+=1
print(c)