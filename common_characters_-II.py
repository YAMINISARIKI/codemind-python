a=input()
a=a.lower()
a=set(a)
b=input()
b=b.lower()
b=set(b)
s=0
for i in a:
    if i!=" ":
        if i in b:
            s=s+1
print(s)