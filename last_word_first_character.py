n=input()
n=n.split()
n=n[::-1]
for i in n:
    for j in i:
        print(j)
        break
    break