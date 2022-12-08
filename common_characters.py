s1=input().lower()
s2=input().lower()
a=""
for i in s1:
    if i in s2 and i not in a:
        a+=i
for i in s2:
    if i in s1 and i not in a:
        a+=i
a=sorted(a)
if len(a)==0:
    print("-1")
else:
    for i in a:
        if i!=" ":
            print(i,end="")