import math

t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    count=0
    for ii in range(0,n):
        if(s[ii]!=s[n-ii-1]):
            count+=1
    print(count//2-count//4)
