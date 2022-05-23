import math

t=int(input())
for i in range(t):
    n,m,x=map(int,input().split())
    if(m==x):
        print(0)
        continue
    print((n*x)//(x+1))
