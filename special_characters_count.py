s=input()
count1=0
count2=0
count3=0
count4=0
for i in s:
    if(ord(i)>=33 and ord(i)<=47):
        count1+=1
    if(ord(i)>=58 and ord(i)<=64):
        count2+=1
    if(ord(i)>=91 and ord(i)<=96):
        count3+=1
    if(ord(i)>=123 and ord(i)<=126):
        count4+=1
print(count1+count2+count3+count4)