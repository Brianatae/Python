year=int(input("enter the year"))
if(year%400==0 or year%4==0):
    print("its a leap year")
else:
    if(year%100==0):
        print("not a leap year")
    else:
        print("all other is not a leap year")