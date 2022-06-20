import math

t=int(input())
for i in range(t):
    a,b,n=map(int,input().split())
    if(a==b):
        print(0)
        continue
    if((a^b)<n):
        print(1)
        continue
    x=(a^b)
    y=math.floor(math.log2(x))
    if(n>2**y):
        print(2)
        continue
    print(-1)
