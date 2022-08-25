x=input()
x=x.split()
max=0
for i in x:
    if max<len(i):
        max=len(i)
print(max)