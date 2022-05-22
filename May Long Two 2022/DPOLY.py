import math

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.reverse()
    for ii in range(0,n):
        if(a[ii]!=0):
            print(n-ii-1)
            break
