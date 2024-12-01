n=int(input("Nhập N:"))
listso=[]
for i in range(0,n):
    BoSo=input("Nhap bo 6 so: ").split()
    listso.append(set(BoSo))
VL=input("Nhap giai db: ").split()
VL=set(VL)
for i in listso:
    if len(1&VL)>= len(i)-1:
        print(i)
