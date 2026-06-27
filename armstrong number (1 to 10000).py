for i in range(1,10001,1):
    b=i
    a=i
    s=0
    n=len(str(i))
    while a>0:
        r=a%10
        s=s+(r**n)
        a=a//10
    if b==s:
        print(b)