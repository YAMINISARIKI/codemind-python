a=input()
l="QWERTYUIOPLKHJGFDSAZCXVBNM"
arr=list(a.split())
c=0
for i in arr:
    for j in i:
        if j in l:
            c+=1
print(c)