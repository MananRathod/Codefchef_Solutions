t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(n%2):    
        x=0
        b=[]
        for ii in range(0,n+1):
            x=x^a[ii]
        for iii in range(0,n+1):
            b.append(x^a[iii])
        b.sort()
        b.pop(0)
        print(*b)
    else:
        x=max(a)
        b=[]
        for iii in range(0,n+1):
            b.append(x^a[iii])
        b.sort()
        b.pop(0)
        print(*b)
        
