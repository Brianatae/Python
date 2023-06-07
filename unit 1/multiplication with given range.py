a=int(input("enter the starting range"))
b=int(input("enter the ending range"))
for i in range(a,b+1):
    for j in range(1,11):
        print(" ",i," * ",j,"=",i*j)