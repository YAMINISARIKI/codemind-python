a=input()
c=0
for i in range(len(a)):
    if i<len(a)-1-i:
        if a[i]!=" " and a[len(a)-1-i]!=" ":
            if a[i] in "aeiouAEIOU" and a[len(a)-i-1] not in "aeiouAEIOU" or a[i] not in "aeiouAEIOU" and a[len(a)-i-1] in "aeiouAEIOU":
                c+=1
print(c)