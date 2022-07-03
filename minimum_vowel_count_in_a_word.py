a=input()
arr=list(a.split())
vow=list("aeiouAEIOU")
ma=100
fl=0
for i in arr:
    c=0
    for j in i:
        if j in vow:
            c+=1
            fl=1
    if ma>c:
        ma=c

print(ma)