def func(n):
    if n<0:
        print("invalid")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (func(n-1)+func(n-2))
    n=int(input("enter the num"))
    print(func(n))