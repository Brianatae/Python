o=0
e=0
n=1
while(n!=-1):
    n=int(input("enter a number : "))
    if (n%2==0):
        e=e+1
    else:
        o=o+1
print("odd : ",o)
print("even : ",e)
