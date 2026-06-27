a=int(input("enter a first number"))   #number enter cheyyan
b=a                                    #number save cheyyan
s=0                                    #sum 
n=len(str(a))                          # a variable ille etra digit ind check cheyyan
while a>0:                             
    r=a%10                             #a variable ille vale ill last digit edukkan
    s=s+(r**n)                          # sum edukkan
    a=a//10                                #  a variable ille last digit povan
if b==s:                                # b and s equal ahnankilu
    print("a is armstrong number")      # a is prime number
else:                                   #allenkilu
    print("a is not armstrong number")  #a is not prime number