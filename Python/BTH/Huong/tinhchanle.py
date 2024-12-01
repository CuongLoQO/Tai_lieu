A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if (A % 2 == 1 and B % 2 == 1 and C % 2 == 1) or (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
    print("Cung tinh chan le")
    
else:
    print("Khac tinh chan le")