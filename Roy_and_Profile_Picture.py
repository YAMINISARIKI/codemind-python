L=int(input())
n=int(input())
for i in range(n):
    W,H=map(int,input().split())
    if W>=L and H>=L:
        if W==H:
            print('ACCEPTED')
        else:
            print('CROP IT')
    else:
        print('UPLOAD ANOTHER')