import math

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=a.count(1)
    y=a.count(0)
    if(x==0):
        print(0)
    elif(y==0):
        print(1)
    else:
        for ii in range(0,n):
            if(ii%2==0):
                y-=1
            if(ii%2!=0):
                x-=1
            if(x==0):
                print(0)
                break
            if(y==0):
                print(1)
                break
