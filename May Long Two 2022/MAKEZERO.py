import math

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for ii in range(0,n):
        x=a[ii]
        while(x>0):
            if(math.floor(math.log2(x)) not in d):
                d[math.floor(math.log2(x))]=1
            x-=(2**math.floor(math.log2(x)))
    print(len(d))
