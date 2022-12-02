a=input()
a=a.split()
x=0
y=0
for i in a:
    x+=ord(max(i))
    y+=ord(min(i))
print(abs(x-y))