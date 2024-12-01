a=float(input("A = "))
b=float(input("B = "))
c=float(input("C = "))
delta=b*b-4*a*c
if delta==0:
    print("phuong trinh co nghiem kep: x= ", str(-b/2/a))
if delta<0:
    print("phuong trinh vo nghiem")
if delta>0:
    print("X1 = " + str((-b+delta**0.5)/2/a))
    print("X2 = " + str((-b-delta**0.5)/2/a))
