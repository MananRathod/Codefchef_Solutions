t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    a=0
    b=0
    if(x%10==0):
        a=(x//10)-1
    else:
        a=x//10
    if(y%10==0):
        b=(y//10)-1
    else:
        b=y//10
    print(abs(a-b))
    
