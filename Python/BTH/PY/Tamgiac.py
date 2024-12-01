a = float(input("A = "))
b = float(input("B = "))
c = float(input("C =  "))
if (a + b > c) and (a + c > b) and (b + c > a) and a>0 and b>0 and c>0:
    print("Dung la tam giac")
else:
    print("Khong la tam giac")
