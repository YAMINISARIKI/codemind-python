x=input()
x=x.split()
min=1000
for i in x:
    if min>len(i):
        min=len(i)
print(min)