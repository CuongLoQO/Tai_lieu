import math

s=1
gt=1
n=int(input("Nhap N duong: "))

for i in range(2,n+1):
    if n==0:
        print("F(0)=1")
    else:
        gt=gt*i
        s=s+gt
print("F(",n,") = ",s,sep="")
