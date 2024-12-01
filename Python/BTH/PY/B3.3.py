def uscln(a, b):
    if (a == 0 or b == 0):
        return a+b
    while (a != b):
        if a > b:
            a=a-b
        else:
            b=b-a
    return a
def bscnn(a,b):
    return int((a*b)/ uscln(a,b))
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
 
