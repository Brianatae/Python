a=int(input("enter a number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if((a+b>=c)and(a+c>=b)and(b+c>=a)):
    print("it is a triangle")
else:
    print("it is not a triangle")
