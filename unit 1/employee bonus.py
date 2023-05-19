salary=int(input("enter the salary"))
service=int(input("enter the year"))
a=2023-service
if(a>10):
    bonus=salary*(10/100)
    print(bonus)
elif(a>6 and a<10):
    bonus=salary*(8/100)
    print(bonus)
else:
    bonus=salary*(5/100)
    print(bonus)