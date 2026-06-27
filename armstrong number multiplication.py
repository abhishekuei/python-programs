a=int(input("enter a first number"))   
b=a                                    
s=0                                    
n=len(str(a))                         
while a>0:                             
    r=a%10                             
    s=s+(r**n)                          
    a=a//10                               
if b==s:                                
    print("a is armstrong number")
    for j in range(1,11,1):
        print(j,"x",b,"=",b*j)      
else:                                   
    print("a is not armstrong number")  