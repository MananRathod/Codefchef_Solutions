t=int(input())
for i in range(t):
    n=int(input())
    a=""
    if(n%2):
        for ii in range(n):
            if(ii%2):
                a+="1"
            else:
                a+="0"
    else:
        for iii in range(n):
            if(iii==0 or iii==n-1):
                a+="1"
            else:
                a+="0"
    print(a)
