name=(input("enter your name"))
age=int(input("enter your age"))
gen=input("enter your gender(M/F)")
n=int(input("enter the number of years"))
p=int(input("enter the principal amount"))
def SI(p,n,r):
    si=(p*n*r)/100
    print("si is",si)
if age>=60:
    r=12
    SI(p,n,r)
elif age<60 and gen=='F':
    r=10
    SI(p,n,r)
elif age<60 and gen=='M':
    r=9
    SI(p,n,r)
else:
    print("invalid")
    
