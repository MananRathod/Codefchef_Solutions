t=int(input())
for i in range(t):
    p,q=map(int,input().split())
    if((p+q)%4==0 or (p+q)%4==1):
        print("Alice")
    else:
        print("Bob")
