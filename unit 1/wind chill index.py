speed=int(input("enter the speed in kmph"))
temp=int(input("enter the temperature"))
windchillindex=13.12+0.6215*temp-11.37*speed**0.16+0.3965*temp*speed*0.16
print(windchillindex)