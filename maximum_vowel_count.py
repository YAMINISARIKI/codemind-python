a=input()
arr=list(a.split())
v="aeiouAEIOU"
m=0
for i in arr:
    c=0
    for j in i:
        if j in v:
            c+=1
    if(m<c):
        m=c
print(m)