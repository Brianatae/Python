o=0
e=0
s=int(input("enter a num"))
en=int(input("enter a num"))
for i in range(s,en+1):
    if(i%2==0):
        e=e+1
    else:
        o=o+1
print("odd : ",o)
print("even : ",e)