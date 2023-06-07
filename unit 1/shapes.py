print("sphere\ncylinder\ncone\nrectangular prism\ntriangular prism")
choice=int(input("enter your choice 1,2,3,4,5:"))
def sphere(pi,r):
    sa=4*3.14*r*r
    vol=(4/3)*3.14*r*r*r
    print("the surface area is",sa)
    print("the vol is",vol)
def cylinder(pi,r,h):
    sa=(2*3.14*r*r)+(2*3.14*r*h)
    vol=3.14*r*r*h
    print("the surface area is",sa)
    print("the vol is",vol)
def cone(pi,r,s,h):
    sa=(3.14*r*s)+(3.14*r*r)
    vol=(1/3)*3.14*r*r*h
    print("the surface area is",sa)
    print("the vol is",vol)
def rectangularprism(l,w,h):
    sa=2*(l*w) +(l*h) +(w*h)
    vol=l*w*h  
    print("the surface area is",sa)
    print("the vol is",vol)
def triangularprism(l,s,b,h):
    sa=(b*h)+2*(l*s)+(l*b)
    vol=1/2*(b*l)*h
    print("the surface area is",sa)
    print("the vol is",vol)
if choice==1:
    r=int(input("enter the radius;",r))
    sphere(3.14,r)
elif choice==2:
    r=int(input("enter the radius;"))
    h=int(input("enter the height:"))
    cylinder(3.14,r,h)
elif choice==3:
    r=int(input("enter the radius"))
    s=int(input("enter the slant height"))
    h=int(input("enter the height"))
    cone(3.14,r,s,h)
elif choice==4:
    l=int(input("enter the length"))
    w=int(input("enter the width"))
    h=int(input("enter the height"))
    rectangularprism(l,w,h)
elif choice==5:
    l=int(input("enter the length"))
    s=int(input("enter the slant height"))
    b=int(input("enter the breadth"))
    h=int(input("enter the height"))
    triangularprism(l,s,b,h)
else:
    print("invalid entry")

