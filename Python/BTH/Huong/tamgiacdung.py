A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if(A + B > C) and (A + C > B) and (B + C > A): 
    print("Dung la tam giac")
    
else:
    print("Khong phai tam giac")