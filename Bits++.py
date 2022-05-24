t=int(input())
res=0
for i in range(t):
    a=input()
    if a=='++X':
        res+=1
    if a=='X++':
        res+=1
    if a=='--X':
        res-=1
    if a=='X--':
        res-=1
print(res)