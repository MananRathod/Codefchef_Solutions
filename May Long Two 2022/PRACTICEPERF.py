import math

a,b,c,d=map(int,input().split())
ans=0
if(a>=10):
    ans+=1
if(b>=10):
    ans+=1
if(c>=10):
    ans+=1
if(d>=10):
    ans+=1
print(ans)
