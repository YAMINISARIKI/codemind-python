n1=input()
n1=n1.lower()
n1=n1.split()
n1=list(n1)
n2=input()
n2=n2.lower()
n2=n2.split()
n2=list(n2)
for i in n2:
    if i in n1:
        if i!=" ":
            print(i,end=" ")