import math

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    h=list(map(int,input().split()))
    a=0
    b=max(h)
    for ii in range(0,n):
        if(h[ii]%x==0):
            a+=(h[ii]//x)
        else:
            a+=(h[ii]//x)+1
    print(min(a,b))
