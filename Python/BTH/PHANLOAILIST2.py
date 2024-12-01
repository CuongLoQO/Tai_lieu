n=int(input("Nhap N: "))
A = []
B = []

for i in range(1,n+1):
    d=input("Nhap gia tri thu "+str(i)+": ")
    try:
        A.append(int(d))
    except:
        try:
            A.append(float(d))
        except:
            B.append(d)
if A!=[]:
    tbc=sum(A)/len(A)
    print("TBC cua A =",tbc)
print("B =",B)

