x = int(input("Nhap N duong: "))
gt = 1
s = 1
for i in range(2,x+1):
        gt*=i
        s+=gt
print("F(",x,") = ",s,sep ="")

