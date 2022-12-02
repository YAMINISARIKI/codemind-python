a=input()
a=a.split()
for i in a:
    print(ord(max(i))-ord(min(i)),end=" ")