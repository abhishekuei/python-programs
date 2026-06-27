f=0
a=int(input("enter a first number"))
if a<=1:
    print("a is not prime number")
else:
    for i in range(2,a):
        if a%i==0:
            f=1
            break
    if f==1:
        print("a is not prime number")
    else:
        print("a is prime number")
        for j in range(1,11,1):
            print(j,"x",a,"=",a*j)