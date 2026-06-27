for a in range(1,101,1):
    if a==1:
        continue
    f=0
    for i in range(2,a):
        if a%i==0:
            f=1
            break
    if f==0:
        print(a)
        for j in range(1,11,1):
            print(j,"x",a,"=",a*j)
