n=int(input("Nhap N: "))
A=[]
B=[]
for i in range(1,n+1):
    d=input("Nhap gia tri thu "+str(i)+": ")
    try:
        A.append(int(d))
    except:
        try:
            A.append(float(d))
        except:
            B.append(d)
if(sum(A)==0):
    print("Tong cac phan tu cua A =",(sum(A)))
else:
    print("Tong cac phan tu cua A =",float(sum(A)))
print(f"B = {sorted(B,reverse=True)}")
