a=input()
a=a.lower()
a=set(a)
b=[]
for i in a:
    if i!=" ":
        x=ord(i)
        b.append(x)
b=set(b)
for i in b:
    print(chr(i),end="")