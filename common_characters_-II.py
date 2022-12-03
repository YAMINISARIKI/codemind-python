n=input()
n=n.lower()
n.split()
n=set(n)
m=input()
m=m.lower()
m.split()
m=set(m)
c=0
for i in n:
    if i!=" ":
        for j in m:
            if i==j:
                c+=1
print(c)