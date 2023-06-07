num=int(input("enter the number"))
def sqrt(num):
        y=int(num**(1/2))
        if(y**2==num):
            print("perfect square")
        else:
            print("not a perfect square")
sqrt(num)
