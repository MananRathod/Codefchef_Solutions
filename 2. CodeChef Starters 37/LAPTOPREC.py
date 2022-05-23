import math

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if(n==1):
        print(a[0])
        continue
    l=[]
    for ii in range(1,11):
        l.append(a.count(ii))
    l.sort()
    if(l[-1]==l[-2]):
        print("CONFUSED")
        continue
    for iii in range(1,11):
        if(a.count(iii)==l[-1]):
            print(iii)
            break
