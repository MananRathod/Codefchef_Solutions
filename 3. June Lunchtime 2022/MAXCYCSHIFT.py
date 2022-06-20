t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    y=[]
    for ii in range(n):
        b=[]
        x=0
        for iii in range(n):
            x=x^a[iii]
            b.append(x)
        s=set(b)
        y.append(len(s))
        a.insert(0,a[-1])
        a.pop()
    y.sort()
    print(y[-1])
