n=input()
x1=0
x2=0
x3=0
y1=0
y2=0
y3=0
for i in n:
    if i=="[":
        x1+=1
    elif i=="]":
        y1+=1
    elif i=="{":
        x2+=1
    elif i=="}":
        y2+=1
    elif i=="(":
        x3+=1
    elif i==")":
        y3+=1
if(x1==y1 and x2==y2 and x3==y3):
    print("True")
else:
    print("False")