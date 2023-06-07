foodrating=int(input("enter the food rating"))
if(foodrating==1):
    print("bad")
elif(foodrating==2):
    print("not bad")
elif(foodrating==3):
    print("average")
elif(foodrating==4):
    print("good")
elif(foodrating==5):
    print("excellent")
servicerating=int(input("enter the service rating"))
if(servicerating==1):
    print("bad")
elif(servicerating==2):
    print("not bad")
elif(servicerating==3):
    print("average")
elif(servicerating==4):
    print("good")
elif(servicerating==5):
    print("excellent")
ambience=int(input("enter the rating"))
if(ambience==1):
    print("bad")
elif(ambience==2):
    print("not bad")
elif(ambience==3):
    print("average")
elif(ambience==4):
    print("good")
elif(ambience==5):
    print("excellent")
bill=int(input("enter the bill amount"))
if(foodrating==4 or foodrating==5):
    if(servicerating==4 or servicerating==5 and ambience==4 or ambience==5):
        tips=bill*(10/100)
    else:
        tips=bill*(5/100)
else:
    if(servicerating==4 or servicerating==5 and ambience==4 or ambience==5):
        tips=bill*(5/100)
    else:
        tips=bill*(1/100)
print("the tip amount is",tips)
        
