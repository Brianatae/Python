name=input("enter the name")
age=int(input("enter the age"))
gender=input("enter M or F")
days=int(input("enter the days"))
if(age>=18 and age<=30 and gender=='F'):
   print(days*750)
elif(age>=30 and age<=40 and gender=='M'):
   print(days*800)
elif(age>=30 and age<=40 and gender=='F'):
   print(days*800)
else:
   print("none")
